from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() 

class Product(BaseModel):
    id: int
    name: str
    price: float

products = [
    {
        "id": 1,
        "name": "iPhone 15",
        "price": 25000000
    },
    {
        "id": 2,
        "name": "Samsung S25",
        "price": 22000000
    },
    {
        "id": 3,
        "name": "Xiaomi 15",
        "price": 15000000
    }
]


@app.get("/")
def home():
    return {
        "message": "Welcome to ShopHub API"
    }


@app.get("/products")
def get_products():
    return products

@app.get("/products/{id}")
def get_product(id: int):
    for product in products:
        if product["id"] == id:
            return product

    return {
        "message": "Product not found"
    }

@app.post("/products")
def create_product(product: Product):
    products.append(product.dict())

    return {
        "message": "Product created successfully",
        "product": product
    }

@app.put("/products/{id}")
def update_product(id: int, updated_product: Product):
    for index, product in enumerate(products):
        if product["id"] == id:
            products[index] = updated_product.dict()

            return {
                "message": "Product updated successfully",
                "product": updated_product
            }

    return {
        "message": "Product not found"
    }

@app.delete("/products/{id}")
def delete_product(id: int):
    for index, product in enumerate(products):
        if product["id"] == id:
            deleted_product = products.pop(index)

            return {
                "message": "Product deleted successfully",
                "product": deleted_product
            }

    return {
        "message": "Product not found"
    }