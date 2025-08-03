from pydantic import BaseModel, Field
from src.app.locations.domain.value_object.name import Name 
from src.app.locations.domain.value_object.description import Description
class Location(BaseModel):
    id: int = Field(..., description="Unique identifier for the location")
    name: Name
    latitude: float
    longitude: float 
    description: Description 
    
