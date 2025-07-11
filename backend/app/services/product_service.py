from app.models.product_model import Product
from app.schemas.product_schema import ProductCreate
from sqlalchemy.orm import Session

def create_product(db: Session, product: ProductCreate):
    new_product = Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def get_all_products(db: Session):
    return db.query(Product).all()