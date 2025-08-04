from pydantic import BaseModel, Field
from typing import Optional

class LocationCreate(BaseModel):
    name: str
    latitude: float
    longitude: float
    description: Optional[str] = None
    category_id: int = Field(..., description="ID de la categoría asociada")
    address: Optional[str] = None
    phone: Optional[str] = None
