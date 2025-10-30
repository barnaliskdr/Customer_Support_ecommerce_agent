from fastapi import APIRouter, HTTPException
from app.services import product_service  # import the service

router = APIRouter(prefix="/products", tags=["Products"])  # 👈 cleaner URL prefix

@router.get("/")
async def get_products():
    products = product_service.get_all_products()
    return {"message": "List of products", "data": products}

@router.get("/{product_id}")
async def get_product_by_id(product_id: int):
    product = product_service.get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product details", "data": product}
