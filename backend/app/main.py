from fastapi import FastAPI
from app.api.v1.routes import auth_routes, product_routes
from app.middleware.request_logger import log_requests
from app.config.settings import settings

app = FastAPI(title="E-Commerce API")

app.include_router(auth_routes.router, prefix="/api/v1/auth")
app.include_router(product_routes.router, prefix="/api/v1/products")

app.middleware("http")(log_requests)
