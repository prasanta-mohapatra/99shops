from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from app.domain.shop.shop_service import ShopService
from app.infrastructure.models.shops import Shop
from app.routes.service_factory import get_shop_service

app = APIRouter()


@app.get("/", response_model=List[Shop], status_code=status.HTTP_200_OK)
async def get_all_shops(
    shop_service: ShopService = Depends(get_shop_service),
) -> List[Shop]:
    try:
        return await shop_service.list_all_shops()
    except HTTPException:
        raise


@app.post("/", response_model=Shop, status_code=status.HTTP_201_CREATED)
async def create_shop(
    shop_details: Shop, shop_service: ShopService = Depends(get_shop_service)
):
    try:
        return await shop_service.create_new_shop(shop_details)
    except HTTPException:
        raise


@app.get("/{shop_id}", response_model=Shop, status_code=status.HTTP_200_OK)
async def get_shop(shop_id: int, shop_service: ShopService = Depends(get_shop_service)):
    try:
        return await shop_service.get_shop_details(shop_id)
    except HTTPException:
        raise


@app.patch("/{shop_id}", response_model=Shop, status_code=status.HTTP_200_OK)
async def update_shop(
    shop_id: int,
    shop_details: Shop,
    shop_service: ShopService = Depends(get_shop_service),
):
    try:
        return await shop_service.update_shop(shop_id, shop_details)
    except HTTPException:
        raise


@app.delete("/{shop_id}", status_code=status.HTTP_200_OK)
async def delete_shop(
    shop_id: int, shop_service: ShopService = Depends(get_shop_service)
):
    try:
        return await shop_service.delete_shop(shop_id)
    except HTTPException:
        raise
