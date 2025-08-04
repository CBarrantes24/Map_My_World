from src.app.locations.domain.repositories.location_repository import LocationRepository
from src.app.locations.domain.entities.location import Location
from src.app.infrastructure.database.db_connection_factory import DatabaseConnectionFactory
from src.app.locations.domain.value_object.name import Name
from src.app.locations.domain.value_object.description import Description
from src.app.locations.domain.entities.location_with_category import LocationWithCategory
from src.app.category.domain.entities.category import Category
from typing import List, Optional


class LocationRepositoryImpl(LocationRepository):
    def get_location_category_recommendations(self) -> list:
        """Sugiere 10 combinaciones de location+category no revisadas en los últimos 30 días, priorizando las nunca revisadas."""
        connection = DatabaseConnectionFactory.get_connection()
        try:
            with connection.cursor() as cursor:
                # Se asume que existe una tabla 'location_category_review' con campos: location_id, category_id, last_reviewed (timestamp)
                cursor.execute("""
                    SELECT l.id, l.name, c.id, c.name, r.last_reviewed
                    FROM locations l
                    JOIN category c ON l.category_id = c.id
                    LEFT JOIN location_category_review r
                    ON l.id = r.location_id AND c.id = r.category_id
                    WHERE r.last_reviewed IS NULL OR r.last_reviewed < (CURRENT_DATE - INTERVAL '30 days')
                    ORDER BY (r.last_reviewed IS NULL) DESC, r.last_reviewed ASC NULLS FIRST
                    LIMIT 10;
                """)
                rows = cursor.fetchall()
                from src.app.locations.domain.entities.location_category_recommendation import LocationCategoryRecommendation
                result = []
                for row in rows:
                    rec = LocationCategoryRecommendation(
                        location_id=row[0],
                        location_name=row[1],
                        category_id=row[2],
                        category_name=row[3],
                        last_reviewed=row[4]
                    )
                    result.append(rec)
                return result
        finally:
            DatabaseConnectionFactory.realease_connection(connection)
    
    def get_locations_with_category(self) -> list:
        """Retrieve all locations with their category data."""
        connection = DatabaseConnectionFactory.get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT l.id, l.name, l.latitude, l.longitude, l.description,
                           c.id, c.name, c.type, c.description
                    FROM locations l
                    JOIN category c ON l.category_id = c.id
                """)
                rows = cursor.fetchall()
                print("rows:",rows) 
                result = []
                for row in rows:
                    category = Category(id=row[5], name=row[6], type=row[7], description=row[8])
                    location_with_category = LocationWithCategory(
                        id=row[0],
                        name=row[1],
                        latitude=row[2],
                        longitude=row[3],
                        description=row[4],
                        category=category,
                        
                    )
                    result.append(location_with_category)
                return result
        finally:
            DatabaseConnectionFactory.realease_connection(connection)

    def get_location(self, location_id: int) -> Optional[Location]:
        """Retrieve a location by its ID."""
        connection = DatabaseConnectionFactory.get_connection()
        try:
              with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, name, description, latitude, longitude, category_id FROM locations WHERE id = %s;", (location_id,))
                row = cursor.fetchone()
                if row:
                    return Location(
                        id=row[0],
                        name=row[1],
                        description=row[2],
                        latitude=row[3],
                        longitude=row[4],
                        category_id=row[5]
                    )
                return None
            
        finally:
            DatabaseConnectionFactory.realease_connection(connection)

    def get_all_locations(self) -> List[Location]:
        """Retrieve all locations."""
        connection = DatabaseConnectionFactory.get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, name, description, longitude, latitude, category_id,create_date,last_updated  FROM locations")
                rows = cursor.fetchall()
                return [Location(
                    id=row[0],
                    name=row[1],
                    description=row[2],
                    longitude=row[3],
                    latitude=row[4],
                    category_id=row[5],
                    create_date=str(row[6]) if len(row) > 6 else None,
                    last_updated=str(row[7]) if len(row) > 7 else None
                ) for row in rows]
        finally:
            DatabaseConnectionFactory.realease_connection(connection)
       

    def add_location(self, location: Location) -> Location:
        """Add a new location."""
        connection = DatabaseConnectionFactory.get_connection()
        try:
            with connection.cursor() as cursor:
                # Validar el nombre usando el Value Object antes de la inserción
                # name_location = Name(value=location.name)
                # description_location = Description(value=location.description)

                cursor.execute(
                    """
                    INSERT INTO locations (name, latitude, longitude, description, category_id, create_date, last_updated)
                    VALUES (%s, %s, %s, %s, %s,  %s, %s) RETURNING id;
                    """,
                    (
                        location.name,
                        location.latitude,
                        location.longitude,
                        location.description,
                        location.category_id,
                        location.create_date,
                        location.last_updated
                    )
                )
                row = cursor.fetchone()
                if row:
                    cursor.execute(
                    '''
                    INSERT INTO location_category_review (location_id, category_id, last_reviewed)
                    VALUES (%s, %s, NOW())
                    ON CONFLICT (location_id, category_id)
                    DO UPDATE SET last_reviewed = NOW();
                    ''', (row[0], location.category_id)
                    )
                
                location_id = row[0]
                connection.commit()
                print(f"Location: {location}")
                return Location(
                    id=location_id,
                    name=location.name,
                    description=location.description,
                    latitude=location.latitude,
                    longitude=location.longitude,
                    category_id=location.category_id,
                    create_date=location.create_date,
                    last_updated=location.last_updated
                )
                
            print("Location added successfully")
                 
        finally:
            DatabaseConnectionFactory.realease_connection(connection)


    def update_location(self, location_id: int, location: Location) -> None:
        """Update an existing location, solo los campos enviados."""
        connection = DatabaseConnectionFactory.get_connection()
        try:
            with connection.cursor() as cursor:
                update_fields = []
                values = []
                # Solo actualiza los campos que no sean None
                if location.name is not None:
                    update_fields.append("name = %s")
                    values.append(location.name)
                if location.description is not None:
                    update_fields.append("description = %s")
                    values.append(location.description)
                if location.latitude is not None:
                    update_fields.append("latitude = %s")
                    values.append(location.latitude)
                if location.longitude is not None:
                    update_fields.append("longitude = %s")
                    values.append(location.longitude)
                if location.category_id is not None:
                    update_fields.append("category_id = %s")
                    values.append(location.category_id)
                if hasattr(location, "address") and location.address is not None:
                    update_fields.append("address = %s")
                    values.append(location.address)
                if hasattr(location, "phone") and location.phone is not None:
                    update_fields.append("phone = %s")
                    values.append(location.phone)
                update_fields.append("last_updated = NOW()")
                sql = f"UPDATE locations SET {', '.join(update_fields)} WHERE id = %s RETURNING id, name, description, latitude, longitude, category_id;"
                values.append(location_id)
                cursor.execute(sql, tuple(values))
                row = cursor.fetchone()
                if row:
                    cursor.execute(
                        '''
                        INSERT INTO location_category_review (location_id, category_id, last_reviewed)
                        VALUES (%s, %s, NOW())
                        ON CONFLICT (location_id, category_id)
                        DO UPDATE SET last_reviewed = NOW();
                        ''', (row[0], row[5])
                    )
                connection.commit()
                if row:
                    return Location(
                        id=row[0],
                        name=row[1],
                        description=row[2],
                        latitude=row[3],
                        longitude=row[4],
                        category_id=row[5]
                    )
                return None
        finally:
            DatabaseConnectionFactory.realease_connection(connection)
  

    def delete_location(self, location_id: int) -> None:
        """Delete a location by its ID."""
        connection = DatabaseConnectionFactory.get_connection()
        try:
            pass
        finally:
            DatabaseConnectionFactory.realease_connection(connection)