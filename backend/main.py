from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import text

from fastapi.security import OAuth2PasswordRequestForm

from database import engine, get_db
from models import Base
import schemas
import crud
import models
import auth

app = FastAPI()

from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm
)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    payload = auth.verify_token(token)

    username = payload.get("sub")

    user = db.query(models.User).filter(
        models.User.username == username
    ).first()

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user

# Tạo bảng nếu chưa có
Base.metadata.create_all(bind=engine)

# Kiểm tra kết nối PostgreSQL
try:
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    print("✅ Connected to PostgreSQL successfully!")
except Exception as e:
    print("❌ Connection failed!")
    print(e)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================
# Home
# ==========================

@app.get("/")
def home():
    return {
        "message": "Welcome to ShopHub API"
    }

# ==========================
# Category APIs
# ==========================

@app.post("/categories", response_model=schemas.CategoryResponse)
def create_category(
    category: schemas.CategoryCreate,
    db: Session = Depends(get_db)
):
    return crud.create_category(db, category)


@app.get("/categories", response_model=list[schemas.CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)


# ==========================
# Product APIs
# ==========================

@app.post("/products", response_model=schemas.ProductResponse)
def create_product(
    product: schemas.ProductCreate,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    auth.check_admin(current_user)

    return crud.create_product(
        db,
        product
    )


@app.get("/products/{product_id}", response_model=schemas.ProductResponse)
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = crud.get_product_by_id(db, product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


@app.put("/products/{product_id}", response_model=schemas.ProductResponse)
def update_product(
    product_id: int,
    product: schemas.ProductCreate,
    db: Session = Depends(get_db)
):
    updated_product = crud.update_product(
        db,
        product_id,
        product
    )

    if updated_product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return updated_product


# ==========================
# Test Validation
# ==========================

@app.post("/test-product")
def test_product(product: schemas.ProductCreate):
    return {
        "message": "Data is valid!",
        "data": product
    }

# ==========================
# DELETE 
# ==========================
@app.delete("/products/{product_id}")
def delete_product(
    product_id: int,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    auth.check_admin(current_user)

    deleted_product = crud.delete_product(
        db,
        product_id
    )

    if deleted_product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return {
        "message": "Product deleted successfully"
    }


# ==========================
#register 
# ==========================
@app.post(
    "/register",
    response_model=schemas.UserResponse
)
def register(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    return crud.create_user(
        db,
        user
    )


@app.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    db_user = crud.authenticate_user(
        db,
        form_data.username,
        form_data.password
    )
    if db_user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    access_token = auth.create_access_token(
        {
            "sub": db_user.username,
            "role": db_user.role
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "username": db_user.username,
        "role": db_user.role
    }

