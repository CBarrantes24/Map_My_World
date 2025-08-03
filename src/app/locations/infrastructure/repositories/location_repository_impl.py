from src.app.locations.domain.repositories.location_repository import LocationRepository
from src.app.locations.domain.entities.location import Location
from src.app.infrastructure.database.db_connection_factory import DatabaseConnectionFactory
from src.app.locations.domain.value_object.name import Name
from src.app.locations.domain.value_object.description import Description
from typing import List, Optional


class LocationRepositoryImpl(LocationRepository):

    def get_location(self, location_id: int) -> Optional[Location]:
        """Retrieve a location by its ID."""
        connection = DatabaseConnectionFactory.get_connection()
        try:
            pass
        finally:
            DatabaseConnectionFactory.release_connection(connection)

    def get_all_locations(self) -> List[Location]:
        """Retrieve all locations."""
        connection = DatabaseConnectionFactory.get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, name, description, longitude, latitude FROM locations")
                rows = cursor.fetchall()
                return [Location(
                    id=row[0],
                    name=Name(value=  row[1]),
                    description=Description (value = row[2]),
                    longitude=row[3],
                    latitude=row[4]
                    ) for row in rows]
        finally:
            DatabaseConnectionFactory.release_connection(connection)
       

    def add_location(self, location: Location) -> None:
        """Add a new location."""
        connection = DatabaseConnectionFactory.get_connection()
        try:
            pass
        finally:
            DatabaseConnectionFactory.release_connection(connection)


    def update_location(self, location: Location) -> None:
        """Update an existing location."""
        connection = DatabaseConnectionFactory.get_connection()
        try:
            pass
        finally:
            DatabaseConnectionFactory.release_connection(connection)
  

    def delete_location(self, location_id: int) -> None:
        """Delete a location by its ID."""
        connection = DatabaseConnectionFactory.get_connection()
        try:
            pass
        finally:
            DatabaseConnectionFactory.release_connection(connection)