from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    stock: int

class ProductOut(ProductCreate):
    id: int
    class Config:
        from_attributes = True