from pydantic import BaseModel, Field
from src.app.locations.domain.value_object.name import Name
from src.app.locations.domain.value_object.description import Description
from typing import Optional
class Location(BaseModel):
    id: int = Field(..., description="Unique identifier for the location")
    name: str
    latitude: float
    longitude: float
    description: str
    category_id: int = Field(..., description="ID de la categoría asociada")
    create_date: Optional[str] = Field(None, description="Timestamp of when the location was created")
    last_updated: Optional[str] = Field(None, description="Timestamp of the last update to the location")
    
    


    # # Para campos opcionales, usa Optional de typing y asigna un valor por defecto (por ejemplo, None):

    # address: Optional[str] = Field(None, description="Dirección opcional de la ubicación")
    # phone: Optional[str] = Field(None, description="Teléfono opcional de la ubicación")




