from sqlalchemy.orm import Session
from security import hash_password, verify_password

import models
import schemas

def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(
        name=category.name
    )

    db.add(db_category)
    db.commit()
    db.refresh(db_category)

    return db_category

def get_categories(db: Session):
    return db.query(models.Category).all()

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(
        name=product.name,
        price=product.price,
        category_id=product.category_id
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product

def get_products(db: Session):
    return db.query(models.Product).all()

def get_product_by_id(db: Session, product_id: int):
    return db.query(models.Product).filter(
        models.Product.id == product_id
    ).first()

def update_product(
    db: Session,
    product_id: int,
    product: schemas.ProductCreate
):
    db_product = db.query(models.Product).filter(
        models.Product.id == product_id
    ).first()

    if db_product is None:
        return None

    db_product.name = product.name
    db_product.price = product.price
    db_product.category_id = product.category_id

    db.commit()
    db.refresh(db_product)

    return db_product

def delete_product(db: Session, product_id: int):
    db_product = db.query(models.Product).filter(
        models.Product.id == product_id
    ).first()

    if db_product is None:
        return None

    db.delete(db_product)
    db.commit()

    return db_product

def create_user(
    db: Session,
    user: schemas.UserCreate
):
    print("===== CREATE USER =====")
    print(user)
    hashed_password = hash_password(user.password)
    
    print("Hash OK")
    

    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )

    print("Model OK")

    db.add(db_user)
    print("Add OK")

    db.commit()
    print("Commit OK")

    db.refresh(db_user)
    print("Refresh OK")

    return db_user

def create_user(
    db: Session,
    user: schemas.UserCreate
):
    hashed_password = hash_password(user.password)

    db_user = models.User(
    username=user.username,
    email=user.email,
    hashed_password=hashed_password,
    role="CUSTOMER"
)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def authenticate_user(
    db: Session,
    username: str,
    password: str
):
    user = db.query(models.User).filter(
        models.User.username == username
    ).first()

    if user is None:
        return None

    if not verify_password(
        password,
        user.hashed_password
    ):
        return None

    return user