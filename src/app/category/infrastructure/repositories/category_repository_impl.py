from src.app.category.domain.repositories.category_repository import CategorynRepository
from src.app.category.domain.entities.category import Category
from src.app.infrastructure.database.db_connection_factory import DatabaseConnectionFactory
from src.app.category.domain.value_object.name import Name
from src.app.category.domain.value_object.description import Description
from typing import List, Optional


class CategoryRepositoryImpl(CategorynRepository):

    def get_category(self, category_id: int) -> Optional[Category]:
        """Retrieve a category by its ID."""
        connection = DatabaseConnectionFactory.get_connection()
        try:
              with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, name, description, type  FROM category WHERE id = %s;", (category_id,))
                row = cursor.fetchone()
                if row:
                    # Crear la instancia utilizando el Value Object
                    return Category(
                        id=row[0],
                        name=row[1],  # Value Object
                        description=row[2],
                        type= row[3]
                    )
                return None
            
        finally:
            DatabaseConnectionFactory.realease_connection(connection)

    def get_all_categories(self) -> List[Category]:
        """Retrieve all category."""
        connection = DatabaseConnectionFactory.get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, name, description, type FROM category")
                rows = cursor.fetchall()
                return [Category(
                    id=row[0],
                    name = row[1],
                    description=row[2],
                    type=row[3],
                    ) for row in rows]
        finally:
            DatabaseConnectionFactory.realease_connection(connection)
       

    def add_category(self, category: Category) -> Category:
        """Add a new category."""
        connection = DatabaseConnectionFactory.get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO category (name,type, description)
                    VALUES (%s, %s, %s) RETURNING id;
                    """,
                    (
                        category.name,
                        category.type,
                        category.description,  # Use the value from the Value Object
                    ) 
                )
                row = cursor.fetchone()  

                category_id = row[0]
                connection.commit()
                
                print(f"Category: {category}")
                return Category(
                    id=category_id,
                    name = category.name,  # Use the value from the Value Object
                    description=category.description,  # Use the value from the Value Object
                    type=category.type,
                )
                
            print("Category added successfully")
                 
        finally:
            DatabaseConnectionFactory.realease_connection(connection)


    def update_category(self, category_id: int,category: Category) -> None:
        """Update an existing category."""
        connection = DatabaseConnectionFactory.get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE category
                    SET name = %s, description = %s, type = %s, 
                    WHERE id = %s RETURNING id, name, description, type;
                """, (
                    category.name,  # Value Object
                    category.description,
                    category.type,
                    category_id # ID del category a actualizar
                ))
                # Confirmar la transacción
                connection.commit()
                
                row = cursor.fetchone()
                if row:
                    return Category(
                        id=row[0],
                        name=row[1],  # Value Object
                        description =row[2],
                        type = row[3]
                    )
                return None
        finally:
            DatabaseConnectionFactory.realease_connection(connection)
  

    def delete_category(self, category_id: int) -> None:
        """Delete a category by its ID."""
        connection = DatabaseConnectionFactory.get_connection()
        try:
            pass
        finally:
            DatabaseConnectionFactory.realease_connection(connection)