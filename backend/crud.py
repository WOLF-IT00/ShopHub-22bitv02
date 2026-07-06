from sqlalchemy.orm import Session

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