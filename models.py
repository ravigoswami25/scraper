from pydantic import BaseModel
from typing import Optional

class Settings(BaseModel):
    pages: Optional[int] = None
    proxy: Optional[str] = None

class Product(BaseModel):
    product_title: str
    product_price: float
    path_to_image: str
