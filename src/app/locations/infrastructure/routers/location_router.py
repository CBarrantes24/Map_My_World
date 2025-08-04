from fastapi import APIRouter, Depends, HTTPException
from src.app.locations.infrastructure.repositories.location_repository_impl import LocationRepositoryImpl
from src.app.locations.application.location_service import LocationService
from src.app.locations.domain.entities.location import Location


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

@router.get("/{location_id}", response_model=Location, summary="Obtener producto por ID")
def get_location(location_id: int, service: LocationService = Depends(get_location_service)):
    location = service.get_location(location_id)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return location

@router.put("/{location_id}", response_model=Location)
def update_producto(location_id: int, location: Location, service: LocationService = Depends(get_location_service)):
    return service.update_location(location_id, location)


@router.post("/", response_model=Location, summary="Add a new location")
def add_location( location: Location,
                   service: LocationService = Depends(get_location_service)):
    return service.add_location(location)
