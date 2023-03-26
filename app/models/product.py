from pydantic import BaseModel


class Product(BaseModel):
    name: str
    manufacturer: str
    price: float
    amount: int
