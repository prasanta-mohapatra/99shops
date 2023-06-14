from app.infrastructure.models import BaseModel
from sqlalchemy import Column, Integer, String, Float


class Shop(BaseModel):
    __tablename__ = "shops"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
