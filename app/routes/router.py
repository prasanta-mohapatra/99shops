from fastapi import APIRouter
from app.routes.shop.route import app

router = APIRouter()

router.include_router(app, prefix="/shop")
