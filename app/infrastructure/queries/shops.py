from typing import List, Optional

from sqlalchemy import func
from sqlmodel import Session, delete, select, update

from app.core.connection import engine
from app.domain.shop.shop_schema import ShopUpdateSchema
from app.infrastructure.models.shops import Shop
from app.utils.exception.internal_exception import ConflictException


class ShopsQueries:
    def __init__(self, db_engine=None) -> None:
        self.__engine = db_engine or engine

    async def get_all_shops(
        self,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
        perimeter: Optional[float] = None,
    ) -> List[Shop]:
        with Session(self.__engine) as session:
            query = select(Shop)
            if latitude and longitude and perimeter:
                """Calculate the distance between the given latitude/longitude and shop coordinates"""
                distance = func.sqrt(
                    func.pow(69.1 * (Shop.latitude - latitude), 2)
                    + func.pow(
                        69.1 * (Shop.longitude - longitude) * func.cos(latitude / 57.3),
                        2,
                    )
                )
                # Query the shops within the specified perimeter
                query = query.where(distance <= perimeter).order_by(distance)
            results = session.exec(query).all()

            return results

    async def get_shop_by_id(self, shop_id: int) -> Shop:
        with Session(self.__engine) as session:
            query = select(Shop).where(Shop.id == shop_id)
            results = session.exec(query).first()
            return results  # type: ignore

    async def create_shop(self, shop: Shop) -> Shop:
        with Session(self.__engine) as session:
            shop_meta = Shop.from_orm(shop)
            try:
                session.add(shop_meta)
                session.commit()
                session.refresh(shop_meta)
                return shop_meta
            except Exception as e:
                session.rollback()
                error_message = str(e.args[0]) if e.args else "Unknown error occurred"
                raise ConflictException(error_message)

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
            return updated_shop  # type: ignore

    async def delete_shop(self, shop_id: int) -> Optional[int]:
        with Session(self.__engine) as session:
            query = delete(Shop).where(Shop.id == shop_id).returning(Shop)
            result = session.execute(query)
            session.commit()
            return result.scalar_one_or_none()
