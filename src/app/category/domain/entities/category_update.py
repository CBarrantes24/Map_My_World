from pydantic import BaseModel, Field
from typing import Optional

class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None
