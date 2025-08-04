from src.app.locations.domain.repositories.location_repository import LocationRepository
from src.app.locations.domain.entities.location import Location
import datetime


class LocationService:
    def get_location_category_recommendations(self) -> list:
        """Sugiere 10 combinaciones de location+category no revisadas en los últimos 30 días, priorizando las nunca revisadas."""
        return self.repository.get_location_category_recommendations()
    def __init__(self, location_repository: LocationRepository):
        self.repository = location_repository
    def get_locations_with_category(self) -> list:
        """Retrieve all locations with their category data."""
        

        
        
        return self.repository.get_locations_with_category()

    def get_location(self, location_id: int) -> Location:
        """Retrieve a location by its ID."""
        return self.repository.get_location(location_id)

    def get_all_locations(self) -> list[Location]:
        """Retrieve all locations."""
        
        return self.repository.get_all_locations()

    def add_location(self, location: Location) -> Location:
        """Add a new location."""
        
        now_str = datetime.datetime.utcnow().isoformat()
        location.create_date = now_str
        location.last_updated  = now_str
        return self.repository.add_location(location)
        

    def update_location(self,location_id:int, location: Location) -> None:
        """Update an existing location."""
        return self.repository.update_location(location_id,location)

    def delete_location(self, location_id: int) -> None:
        """Delete a location by its ID."""
        self.repository.delete_location(location_id)