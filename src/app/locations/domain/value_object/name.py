from pydantic import BaseModel, Field, field_validator

class Name(BaseModel):
    
    value: str = Field(..., description="The name value")
    
    @field_validator("value")
    def validator_name(cls, v):
        if not v or not isinstance(v, str) or len(v.strip()) == 0:
            raise ValueError("Name must be a non-empty string")
        return v.strip()
    
    def __eq__(self, other):
        return isinstance(other, Name) and self.value == other.value
    
    def __str__(self):
        return self.value