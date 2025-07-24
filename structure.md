# Estructura del Proyecto Map My World

```
map_my_world/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Punto de entrada de la aplicación
│   ├── config.py              # Configuración de la aplicación
│   ├── database.py            # Configuración de la base de datos
│   │
│   ├── models/                # Modelos de SQLAlchemy
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── location.py
│   │   ├── category.py
│   │   └── location_category_reviewed.py
│   │
│   ├── schemas/               # Esquemas de Pydantic
│   │   ├── __init__.py
│   │   ├── location.py
│   │   ├── category.py
│   │   └── recommendation.py
│   │
│   ├── repositories/          # Capa de acceso a datos
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── location.py
│   │   ├── category.py
│   │   └── recommendation.py
│   │
│   ├── services/             # Lógica de negocio
│   │   ├── __init__.py
│   │   ├── location.py
│   │   ├── category.py
│   │   └── recommendation.py
│   │
│   ├── api/                  # Endpoints de la API
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── endpoints/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── locations.py
│   │   │   │   ├── categories.py
│   │   │   │   └── recommendations.py
│   │   │   └── api.py
│   │   └── deps.py           # Dependencias
│   │
│   └── core/                 # Utilidades y configuraciones core
│       ├── __init__.py
│       ├── exceptions.py
│       └── utils.py
│
├── alembic/                  # Migraciones de base de datos
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
│
├── tests/                    # Tests
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_locations.py
│   ├── test_categories.py
│   └── test_recommendations.py
│
├── alembic.ini
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── docker-compose.yml
```