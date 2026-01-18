from pydantic import BaseModel, Field


class Order(BaseModel):
    ...


class OrderCreate(BaseModel):
    ...


class OrderResponse(BaseModel):
    order_id: int
    status: str