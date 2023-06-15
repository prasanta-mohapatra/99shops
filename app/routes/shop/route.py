from typing import List
from fastapi import APIRouter, Depends, status
from app.domain.shop.shop_service import ShopService
from app.infrastructure.models.shops import Shop
from app.routes.service_factory import get_shop_service

app = APIRouter()


@app.get("/", response_model=List[Shop])
async def get_all_shops(
    shop_service: ShopService = Depends(get_shop_service),
) -> List[Shop]:
    try:
        await shop_service.get_all_shops()
    except Exception:
        raise


@app.post("/", response_model=Shop, status_code=status.HTTP_201_CREATED)
async def create_shop(shop_service: ShopService = Depends(get_shop_service)):
    # Your logic for creating a shop goes here
    pass


@app.get("/{shop_id}", response_model=Shop, status_code=status.HTTP_200_OK)
async def get_shop(shop_id: int, shop_service: ShopService = Depends(get_shop_service)):
    # Your logic for retrieving a specific shop goes here
    pass


@app.patch("/{shop_id}", response_model=Shop, status_code=status.HTTP_200_OK)
async def update_shop(shop_id: int):
    # Your logic for updating a specific shop goes here
    pass


@app.delete("/{shop_id}", status_code=status.HTTP_200_OK)
async def delete_shop(shop_id: int):
    # Your logic for deleting a specific shop goes here
    pass
