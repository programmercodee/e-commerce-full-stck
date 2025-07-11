from sqlalchemy import Column, Integer, String, DECIMAL
from app.database.connection import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500))
    price = Column(DECIMAL(10, 2), nullable=False)
    stock = Column(Integer, default=0)