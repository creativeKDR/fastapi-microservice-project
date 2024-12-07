from pydantic import Field
from pydantic.main import BaseModel


class OrderRequest(BaseModel):
    product_id: str = Field(min_length=1)
    price: float = Field(gt=0)
    total: float = Field(gt=0)
    quantity: float = Field(gt=0)
    status: str = Field(min_length=3, max_length=500)

    class Config:
        orm_mode = True


class OrderResponse(BaseModel):
    id: int
    product_id: str = Field(min_length=1)
    price: float = Field(gt=0)
    total: float = Field(gt=0)
    quantity: float = Field(gt=0)
    status: str = Field(min_length=3, max_length=500)

    class Config:
        orm_mode = True
