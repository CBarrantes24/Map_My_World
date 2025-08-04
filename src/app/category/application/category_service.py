from src.app.category.domain.repositories.category_repository import CategorynRepository
from src.app.category.domain.entities.category import Category


class categoryService:
    def __init__(self, category_repository: CategorynRepository):
        self.repository = category_repository

    def get_category(self, category_id: int) -> Category:
        """Retrieve a category by its ID."""
        return self.repository.get_category(category_id)

    def get_all_categories(self) -> list[Category]:
        """Retrieve all categorys."""
        
        return self.repository.get_all_categories()

    def add_category(self, category: Category) -> Category:
        """Add a new category."""
        return self.repository.add_category(category)
        

    def update_category(self,category_id:int, category: Category) -> None:
        """Update an existing category."""
        return self.repository.update_category(category_id,category)

    def delete_category(self, category_id: int) -> None:
        """Delete a category by its ID."""
        self.repository.delete_category(category_id)