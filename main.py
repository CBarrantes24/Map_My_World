from typing import Union
from fastapi import FastAPI
# from shared.infrastructure.api import router as shared_router
from src.app.locations.infrastructure.routers.location_router import router as location_router
from src.app.infrastructure.database.db_connection_factory import DatabaseConnectionFactory

app = FastAPI(title="FastAPI Map My World")

# @app.on_event("startup")
# async def startup_event():
#     # Initialize database connection
#     await DatabaseConnectionFactory.initialize()
    
# @app.on_event("shutdown")
# async def shutdown_event():
#     # Close all database connections
#     print("Closing all database connections...")
#     await DatabaseConnectionFactory.close_all_connections()

app.include_router(location_router, prefix="/api/v1", tags=["locations"])

