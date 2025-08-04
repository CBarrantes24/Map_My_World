from pydantic import BaseModel, Field
from src.app.category.domain.value_object.name import Name 
from src.app.category.domain.value_object.description import Description
class Category(BaseModel):
    id: int = Field(..., description="Unique identifier for the category")
    name: str
    type: str
    description: str 
    
    
    
