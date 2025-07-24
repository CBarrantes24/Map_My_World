from sqlalchemy import Column, String, Float, Index
from sqlalchemy.orm import relationship
from app.models.base import BaseModel


class Location(BaseModel):
    """
    Location model representing geographical locations
    """
    __tablename__ = "locations"
    
    name = Column(String(255), nullable=False, index=True)
    description = Column(String(1000), nullable=True)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    address = Column(String(500), nullable=True)
    
    # Relationships
    reviews = relationship("LocationCategoryReviewed", back_populates="location")
    
    # Indexes for efficient geospatial queries
    __table_args__ = (
        Index('idx_location_coordinates', 'longitude', 'latitude'),
    )
    
    def __repr__(self):
        return f"<Location(id={self.id}, name='{self.name}', lat={self.latitude}, lon={self.longitude})>"