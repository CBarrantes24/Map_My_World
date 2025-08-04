from pydantic import BaseModel, Field
from src.app.locations.domain.value_object.name import Name 
from src.app.locations.domain.value_object.description import Description
class Location(BaseModel):
    id: int = Field(..., description="Unique identifier for the location")
    name: str
    latitude: float
    longitude: float 
    description: str 
    category_id: int = Field(..., description="ID de la categoría asociada")
    
    
    
