from typing import Optional
from pydantic import BaseModel


class ShopUpdateSchema(BaseModel):
    name: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    country: Optional[str]
    postal_code: Optional[str]
