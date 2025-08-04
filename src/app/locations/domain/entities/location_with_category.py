from pydantic import BaseModel
from src.app.locations.domain.entities.location import Location
from src.app.category.domain.entities.category import Category

class LocationWithCategory(BaseModel):
    id: int
    name: str
    latitude: float
    longitude: float
    description: str
    category: Category
