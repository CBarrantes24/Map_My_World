from pydantic import BaseModel, Field
from typing import Optional

class CategoryCreate(BaseModel):
    name: str
    type: Optional[str] = None
    description: Optional[str] = None
