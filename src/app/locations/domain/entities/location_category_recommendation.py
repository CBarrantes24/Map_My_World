from pydantic import BaseModel
from datetime import datetime

class LocationCategoryRecommendation(BaseModel):
    location_id: int
    location_name: str
    category_id: int
    category_name: str
    last_reviewed: datetime | None
