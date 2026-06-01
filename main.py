from fastapi import FastAPI

from app.api.products import router as products_router

from app.core.database import engine
from app.models.product_model import ProductDB

app = FastAPI()

ProductDB.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Backend is working"}

app.include_router(products_router)