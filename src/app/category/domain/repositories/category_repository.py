from abc import ABC, abstractmethod
from typing import List, Optional
from src.app.category.domain.entities.category import Category

class CategorynRepository(ABC):
    @abstractmethod
    def get_category(self, category_id: int) -> Optional[Category]:
        """Retrieve a category by its ID."""
        pass

    @abstractmethod
    def get_all_categories(self) -> List[Category]:
        """Retrieve all categorys."""
        pass

    @abstractmethod
    def add_category(self, category: Category) -> Category:
        """Add a new category."""
        pass

    @abstractmethod
    def update_category(self, category_id: int, category: Category) -> Optional[Category]:
        """Update an existing category."""
        pass

    @abstractmethod
    def delete_category(self, category_id: int) -> None:
        """Delete a category by its ID."""
        pass
