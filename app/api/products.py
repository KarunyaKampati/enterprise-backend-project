from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Product(BaseModel):
    id: int
    name: str
    price: float

products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 50000
    },
    {
        "id": 2,
        "name": "Phone",
        "price": 20000
    }
]

@router.get("/products")
def get_products():
    return products

@router.post("/products")
def create_product(product: Product):
    products.append(product.dict())
    return {
        "message": "Product added successfully",
        "product": product
    }
@router.get("/products/{product_id}")
def get_product(product_id: int):

    for product in products:
        if product["id"] == product_id:
            return product

    return {"message": "Product not found"}
@router.delete("/products/{product_id}")
def delete_product(product_id: int):

    for product in products:
        if product["id"] == product_id:
            products.remove(product)

            return {
                "message": "Product deleted successfully"
            }

    return {
        "message": "Product not found"
    }