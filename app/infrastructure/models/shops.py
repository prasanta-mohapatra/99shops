from sqlmodel import SQLModel, Field


class Shop(SQLModel, table=True):
    __tablename__: str = "shops"
    id: int = Field(default=None, primary_key=True)
    name: str = Field(sa_column_kwargs={"nullable": False})
    latitude: float = Field(sa_column_kwargs={"nullable": False})
    longitude: float = Field(sa_column_kwargs={"nullable": False})
    address: str = Field(default=None, sa_column_kwargs={"nullable": True})
    city: str = Field(default=None, sa_column_kwargs={"nullable": True})
    state: str = Field(default=None, sa_column_kwargs={"nullable": True})
    country: str = Field(default=None, sa_column_kwargs={"nullable": True})
    postal_code: str = Field(default=None, sa_column_kwargs={"nullable": True})
