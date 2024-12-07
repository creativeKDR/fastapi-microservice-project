from typing import List, Any

from fastapi import HTTPException
from starlette import status

from sqlalchemy.orm import Session
from src.models import Order
from src.schemas import OrderRequest


class OrderRepository:

    async def get_all_orders(self, db: Session) -> List[Order]:
        return db.query(Order).all()

    async def get_order_by_id(self, db: Session, order_id: int) -> Order:
        return db.query(Order).filter(Order.id == order_id).first()

    async def create_order(self, db: Session, order_request: OrderRequest) -> Order:
        new_order = Order(**order_request.dict())
        db.add(new_order)
        db.commit()
        return new_order

    async def update_order(self, db: Session, order_request: OrderRequest, order_id: int) -> Order:
        order = db.query(Order).filter(Order.id == order_id).first()
        if order is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Order not found')
        # Update order fields from request
        for var, value in vars(order_request).items():
            setattr(order, var, value) if value else None

        db.commit()
        return order

    async def delete_order(self, db: Session, order_id: int) -> Any:
        order = db.query(Order).filter(Order.id == order_id).first()
        if order is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Order not found')
        db.delete(order)
        db.commit()
        return order
