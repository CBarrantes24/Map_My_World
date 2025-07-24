from sqlalchemy import Column, Integer, ForeignKey, DateTime, Text, Index
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.models.base import BaseModel


class LocationCategoryReviewed(BaseModel):
    """
    Model representing the review status of location-category combinations
    """
    __tablename__ = "location_category_reviewed"
    
    location_id = Column(Integer, ForeignKey("locations.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    reviewed_at = Column(DateTime(timezone=True), server_default=func.now())
    review_notes = Column(Text, nullable=True)
    reviewer = Column(Text, nullable=True)  # Could be user ID or system identifier
    
    # Relationships
    location = relationship("Location", back_populates="reviews")
    category = relationship("Category", back_populates="reviews")
    
    # Indexes for efficient queries
    __table_args__ = (
        Index('idx_location_category', 'location_id', 'category_id'),
        Index('idx_reviewed_at', 'reviewed_at'),
    )
    
    def __repr__(self):
        return f"<LocationCategoryReviewed(location_id={self.location_id}, category_id={self.category_id}, reviewed_at={self.reviewed_at})>"