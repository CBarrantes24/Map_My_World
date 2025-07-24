from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.models.base import BaseModel


class Category(BaseModel):
    """
    Category model representing types of places (restaurants, parks, museums, etc.)
    """
    __tablename__ = "categories"
    
    name = Column(String(100), nullable=False, unique=True, index=True)
    description = Column(String(500), nullable=True)
    icon = Column(String(50), nullable=True)  # For UI representation
    
    # Relationships
    reviews = relationship("LocationCategoryReviewed", back_populates="category")
    
    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}')>"