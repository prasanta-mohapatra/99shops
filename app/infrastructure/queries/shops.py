from typing import List

from sqlmodel import Session, delete, select, update

from app.core.connection import engine
from app.domain.shop.shop_schema import ShopUpdateSchema
from app.infrastructure.models.shops import Shop


class ShopsQueries:
    def __init__(self, db_engine=None) -> None:
        self.__engine = db_engine or engine

    async def get_all_shops(self) -> List[Shop]:
        with Session(self.__engine) as session:
            query = select(Shop)
            results = session.exec(query).all()
            return results

    async def get_shop_by_id(self, shop_id: int) -> Shop:
        with Session(self.__engine) as session:
            query = select(Shop).where(Shop.id == shop_id)
            results = session.exec(query).first()
            return results

    async def create_shop(self, shop: Shop) -> Shop:
        with Session(self.__engine) as session:
            shop_meta = Shop.from_orm(shop)
            session.add(shop_meta)
            session.commit()
            session.refresh(shop_meta)
            return shop_meta

    async def update_shop(self, shop_id: int, shop: ShopUpdateSchema) -> Shop:
        with Session(self.__engine) as session:
            query = (
                update(Shop)
                .where(Shop.id == shop_id)
                .values(shop.dict(exclude_none=True))
                .returning(Shop)
            )
            result = session.execute(query)
            session.commit()
            updated_shop = result.fetchone()
            return updated_shop

    async def delete_shop(self, shop_id: int) -> int:
        with Session(self.__engine) as session:
            query = delete(Shop).where(Shop.id == shop_id).returning(Shop)
            result = session.execute(query)
            session.commit()
            return result.scalar_one_or_none()
