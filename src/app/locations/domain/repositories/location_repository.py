from abc import ABC, abstractmethod
from typing import List, Optional
from src.app.locations.domain.entities.location import Location

class LocationRepository(ABC):
    @abstractmethod
    def get_location(self, location_id: int) -> Optional[Location]:
        """Retrieve a location by its ID."""
        pass

    @abstractmethod
    def get_all_locations(self) -> List[Location]:
        """Retrieve all locations."""
        pass

    @abstractmethod
    def add_location(self, location: Location) -> None:
        """Add a new location."""
        pass

    @abstractmethod
    def update_location(self, location: Location) -> None:
        """Update an existing location."""
        pass

    @abstractmethod
    def delete_location(self, location_id: int) -> None:
        """Delete a location by its ID."""
        pass
