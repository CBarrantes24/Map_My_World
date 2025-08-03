from fastapi import APIRouter, Depends
from src.app.locations.infrastructure.repositories.location_repository_impl import LocationRepositoryImpl
from src.app.locations.application.location_service import LocationService
from src.app.locations.domain.entities.location import Location


router = APIRouter()

def get_location_service():
    repository = LocationRepositoryImpl()  # Assuming you have a way to instantiate this
    return LocationService(repository)

@router.get("/",response_model=list[Location], summary="Get all locations")
def get_locations(service: LocationService = Depends(get_location_service)):
    """
    Retrieve all locations.
    """
    return service.get_all_locations()
