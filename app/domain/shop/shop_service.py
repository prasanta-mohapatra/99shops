from typing import List
from app.infrastructure.models.shops import Shop
from app.infrastructure.queries.shops import ShopsQueries


class ShopService:
    def __init__(self):
        self.__shop_queries = ShopsQueries()

    async def list_all_shops(self) -> List[Shop]:
        return await self.__shop_queries.get_all_shops()

    async def get_shop_details(self, shop_id: int) -> Shop:
        pass

    async def create_new_shop(self, shop_details: Shop) -> Shop:
        return await self.__shop_queries.create_shop(shop_details)

    async def update_shop(self, shop_id: int) -> Shop:
        pass

    async def delete_shop(self, shop_id: int) -> None:
        pass
