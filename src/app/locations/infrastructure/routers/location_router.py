from fastapi import APIRouter, Depends, HTTPException
from src.app.locations.infrastructure.repositories.location_repository_impl import LocationRepositoryImpl
from src.app.locations.application.location_service import LocationService
from src.app.locations.domain.entities.location import Location
from src.app.locations.domain.entities.location_update import LocationUpdate
from src.app.locations.domain.entities.location_create import LocationCreate
from src.app.locations.domain.entities.location_category_recommendation import LocationCategoryRecommendation


router = APIRouter(prefix="/locations", tags=["locations"])

from src.app.locations.domain.entities.location_with_category import LocationWithCategory

def get_location_service():
    repository = LocationRepositoryImpl()  # Assuming you have a way to instantiate this
    return LocationService(repository)

@router.get("/",response_model=list[Location], summary="Get all locations")
def get_locations(service: LocationService = Depends(get_location_service)):
    return service.get_all_locations()


@router.get("/with-category", response_model=list[LocationWithCategory], summary="Get all locations with category data")
def get_locations_with_category(service: LocationService = Depends(get_location_service)):
    return service.get_locations_with_category()


@router.get("/recommendations", response_model=list[LocationCategoryRecommendation], summary="Get location+category recommendations")
def get_location_category_recommendations(service: LocationService = Depends(get_location_service)):
    return service.get_location_category_recommendations()

@router.get("/{location_id}", response_model=Location, summary="Obtener producto por ID")
def get_location(location_id: int, service: LocationService = Depends(get_location_service)):
    location = service.get_location(location_id)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return location


@router.put("/{location_id}", response_model=Location)
def update_producto(location_id: int, location_data: LocationUpdate, service: LocationService = Depends(get_location_service)):
    # Obtener la location actual
    current = service.get_location(location_id)
    if not current:
        raise HTTPException(status_code=404, detail="Location not found")
    # Actualizar solo los campos enviados
    update_fields = location_data.dict(exclude_unset=True)
    updated = current.copy(update=update_fields)
    return service.update_location(location_id, updated)



@router.post("/", response_model=Location, summary="Add a new location")
def add_location(location_data: LocationCreate, service: LocationService = Depends(get_location_service)):
    # Mapear LocationCreate a Location (sin id, fechas, etc.)
    location = Location(
        id=0,  # El id se ignora y lo asigna la base de datos
        name=location_data.name,
        latitude=location_data.latitude,
        longitude=location_data.longitude,
        description=location_data.description or "",
        category_id=location_data.category_id,
        create_date=None,
        last_updated=None
        # address=location_data.address,
        # phone=location_data.phone
    )
    return service.add_location(location)
