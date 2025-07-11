from fastapi import FastAPI
from app.api.v1.routes import auth_routes, user_routes, product_routes
from app.config.settings import settings
from app.database.connection import engine, Base

app = FastAPI(title="E-Commerce API")

# Initialize DB
Base.metadata.create_all(bind=engine)

# Routes
app.include_router(auth_routes.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(user_routes.router, prefix="/api/v1/users", tags=["User"])
app.include_router(product_routes.router, prefix="/api/v1/products", tags=["Product"])