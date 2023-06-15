from typing import List

from app.domain.shop.shop_schema import ShopUpdateSchema
from app.infrastructure.models.shops import Shop
from app.infrastructure.queries.shops import ShopsQueries
from app.utils.exception.internal_exception import NotFoundException


class ShopService:
    def __init__(self):
        self.__shop_queries = ShopsQueries()

    async def list_all_shops(self) -> List[Shop]:
        return await self.__shop_queries.get_all_shops()

    async def get_shop_details(self, shop_id: int) -> Shop:
        shop = await self.__shop_queries.get_shop_by_id(shop_id)
        if not shop:
            raise NotFoundException("shop id", shop_id)
        return shop

    async def create_new_shop(self, shop_details: Shop) -> Shop:
        return await self.__shop_queries.create_shop(shop_details)

    async def update_shop(
        self,
        shop_id: int,
        shop_details: ShopUpdateSchema,
    ) -> Shop:
        shop = await self.__shop_queries.update_shop(shop_id, shop_details)
        if not shop:
            raise NotFoundException("shop id", shop_id)
        return shop

    async def delete_shop(self, shop_id: int) -> int:
        shop = await self.__shop_queries.delete_shop(shop_id)
        if not shop:
            raise NotFoundException("shop id", shop_id)
        return shop
