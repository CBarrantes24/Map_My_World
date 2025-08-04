from fastapi import APIRouter, Depends, HTTPException
from src.app.category.infrastructure.repositories.category_repository_impl import CategoryRepositoryImpl
from src.app.category.application.category_service import categoryService
from src.app.category.domain.entities.category import Category


router = APIRouter(prefix="/category", tags=["category"])

def get_category_service():
    repository = CategoryRepositoryImpl()  # Assuming you have a way to instantiate this
    return categoryService(repository)

@router.get("/",response_model=list[Category], summary="Get all categories")
def get_categories(service: categoryService = Depends(get_category_service)):
    return service.get_all_categories()

@router.get("/{category_id}", response_model=Category, summary="Obtener producto por ID")
def get_category(category_id: int, service: categoryService = Depends(get_category_service)):
    category = service.get_category(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="category not found")
    return category

@router.put("/{category_id}", response_model=Category)
def update_producto(category_id: int, category: Category, service: categoryService = Depends(get_category_service)):
    return service.update_category(category_id, category)


@router.post("/", response_model=Category, summary="Add a new category")
def add_category( category: Category,
                   service: categoryService = Depends(get_category_service)):
    return service.add_category(category)
