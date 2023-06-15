from typing import List, Optional, Tuple

import requests

from app.core.config import settings
from app.domain.shop.shop_schema import ShopUpdateSchema
from app.infrastructure.models.shops import Shop
from app.infrastructure.queries.shops import ShopsQueries
from app.utils.exception.internal_exception import NotFoundException


class ShopService:
    def __init__(self):
        self.__shop_queries = ShopsQueries()

    async def get_altitude_longitude(
        self,
        location: str,
    ) -> Tuple[float, float]:
        headers = {
            "User-Agent": f"{settings.APP_NAME}/{settings.APP_VERSION} ({settings.CONTACT})"
        }

        # Construct the API request URL
        url = f"{settings.NOMINATION_URL}/search?q={location}&format=json"

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()

            if data:
                # Extract the latitude and longitude from the first result
                latitude = float(data[0]["lat"])
                longitude = float(data[0]["lon"])
                return latitude, longitude
            else:
                # Handle the case when no results are found
                raise Exception("No results found for the location")

        except requests.RequestException as e:
            # Handle any request errors
            raise Exception(f"Request error: {str(e)}")

        except (KeyError, IndexError):
            # Handle any data parsing errors
            raise Exception("Invalid response from the API")

    async def list_all_shops(
        self,
        location: Optional[str],
        perimeter: float,
    ) -> List[Shop]:
        if location:
            latitude, longitude = await self.get_altitude_longitude(location)
            return await self.__shop_queries.get_all_shops(
                latitude, longitude, perimeter
            )
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
