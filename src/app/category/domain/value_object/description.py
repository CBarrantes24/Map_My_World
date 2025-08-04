from pydantic import BaseModel, Field, field_validator

class Description(BaseModel):
    
    description: str = Field(..., description="The description for the location")
    
    @field_validator("description")
    def validator_description(cls, v):
        if not v or not isinstance(v, str) or len(v.strip()) == 0:
            raise ValueError("Description must be a non-empty string")
        return v.strip()
    
    def __eq__(self, other):
        return isinstance(other, Description) and self.description == other.description
    
    def __str__(self):
        return self.description