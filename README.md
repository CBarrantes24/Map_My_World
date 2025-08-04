# Map My World

## Overview
Map My World is a backend application built with FastAPI for managing locations and categories, including advanced endpoints for recommendations and health checks. The project follows a modular architecture with clear separation between domain, infrastructure, and shared layers.

## Features
- CRUD operations for Locations and Categories
- Recommendation endpoint for location-category combinations not recently reviewed
- Health check endpoint (`/`)
- Modular structure for scalability and maintainability
- Pydantic models for data validation
- Automated tests with pytest

## Folder Structure
```
main.py                       # FastAPI app entry point
requirements.txt              # Python dependencies
pytest.ini                    # Pytest configuration
src/
  app/
    locations/
      domain/
        entities/             # Location models (Location, LocationCreate, LocationUpdate, etc.)
        repositories/         # Location repository interfaces
      infrastructure/
        repositories/         # Location repository implementations
        routers/              # FastAPI routers for location endpoints
      application/            # Location service layer
    category/
      domain/
        entities/             # Category models (Category, CategoryCreate, CategoryUpdate, etc.)
        repositories/         # Category repository interfaces
      infrastructure/
        repositories/         # Category repository implementations
        routers/              # FastAPI routers for category endpoints
      application/            # Category service layer
  shared/
    test/
      infrastructure/         # Test files (e.g., test_health.py)
```

## How to Run
1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Start the application:**
   ```bash
   uvicorn main:app --reload
   ```
3. **Run tests:**
   ```bash
   pytest
   ```

4. **Database Create Table**
    CREATE TABLE category (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        type VARCHAR(50),
        description TEXT
    );

    CREATE TABLE locations (
    id            SERIAL PRIMARY KEY,
    name          VARCHAR(255)      NOT NULL,
    latitude      DOUBLE PRECISION  NOT NULL,
    longitude     DOUBLE PRECISION  NOT NULL,
    description   TEXT              NOT NULL,
    category_id   INTEGER           NOT NULL,
    create_date   TIMESTAMP WITH TIME ZONE,
    last_updated  TIMESTAMP WITH TIME ZONE,
    FOREIGN KEY (category_id) REFERENCES category(id)
    );


    CREATE TABLE location_category_review (
        id SERIAL PRIMARY KEY,
        location_id INTEGER NOT NULL,
        category_id INTEGER NOT NULL,
        last_reviewed TIMESTAMP,
        UNIQUE (location_id, category_id),
        FOREIGN KEY (location_id) REFERENCES locations(id),
        FOREIGN KEY (category_id) REFERENCES category(id)
    );

## Main Endpoints
- `/` : Health check
- `/locations` : Location CRUD, recommendations, and category-combined endpoints
- `/category` : Category CRUD endpoints

## Technologies Used
- FastAPI
- Pydantic
- PostgreSQL (recommended)
- Pytest

## Author
CBarrantes24

---

## Quick Start
1. Clone the repository
2. Install dependencies
3. Configure your database connection in the infrastructure layer if needed
4. Run the server and access the API docs at `/docs`

## API Documentation
Interactive API documentation is available at `/docs` when the server is running.

## Contribution
Feel free to fork the project and submit pull requests for improvements or new features.
