from pydantic import BaseModel, Field
from typing import Optional

class LocationUpdate(BaseModel):
    name: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    description: Optional[str] = None
    category_id: Optional[int] = None
    address: Optional[str] = None
    phone: Optional[str] = None
