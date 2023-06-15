from typing import List

from sqlmodel import Session, select
from app.core.connection import engine
from app.infrastructure.models.shops import Shop


class ShopsQueries:
    def __init__(self, db_engine=None) -> None:
        self.__engine = db_engine or engine

    async def get_all_shops(self) -> List[Shop]:
        with Session(self.__engine) as session:
            query = select(Shop)
            results = session.exec(query).all()
            return results

    async def create_shop(self, shop: Shop):
        with Session(self.__engine) as session:
            shop_meta = Shop.from_orm(shop)
            session.add(shop_meta)
            session.commit()
            session.refresh(shop_meta)
            return shop_meta
