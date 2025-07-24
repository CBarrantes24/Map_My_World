from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # Database
    database_url: str = "postgresql://user:password@localhost:5432/map_my_world"
    database_url_test: str = "postgresql://user:password@localhost:5432/map_my_world_test"
    
    # API
    api_v1_str: str = "/api/v1"
    project_name: str = "Map My World API"
    project_description: str = "API for exploring and reviewing locations around the world"
    version: str = "1.0.0"
    
    # CORS
    backend_cors_origins: list[str] = ["http://localhost:3000", "http://localhost:8080"]
    
    # Application
    debug: bool = False
    environment: str = "development"
    
    # Recommendations
    recommendation_limit: int = 10
    review_expiry_days: int = 30

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()