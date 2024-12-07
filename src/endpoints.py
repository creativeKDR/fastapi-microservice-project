from typing import List

from fastapi import APIRouter, HTTPException, Depends
from starlette import status
from sqlalchemy.orm import Session

from src.repository import OrderRepository
from src.schemas import OrderResponse, OrderRequest
from src.db import get_db

order_router = APIRouter(prefix='/api', tags=['Order'])


@order_router.get('/order', status_code=status.HTTP_200_OK, response_model=List[OrderResponse])
async def get_orders(repository: OrderRepository = Depends(OrderRepository), db: Session = Depends(get_db)):
    response = await repository.get_all_orders(db=db)
    return response


@order_router.get('/order/{order_id}', status_code=status.HTTP_200_OK, response_model=OrderResponse)
async def get_order(order_id: int, repository: OrderRepository = Depends(OrderRepository),
                    db: Session = Depends(get_db)):
    response = await repository.get_order_by_id(db=db, order_id=order_id)
    if response is not None:
        return response
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Order not found')


@order_router.post('/order', status_code=status.HTTP_200_OK, response_model=OrderResponse)
async def create_order(order_request: OrderRequest, repository: OrderRepository = Depends(OrderRepository),
                       db: Session = Depends(get_db)):
    response = await repository.create_order(db=db, order_request=order_request)
    return response


@order_router.put('/order/{order_id}', status_code=status.HTTP_200_OK, response_model=OrderResponse)
async def update_order(order_id: int, order_request: OrderRequest,
                       repository: OrderRepository = Depends(OrderRepository), db: Session = Depends(get_db)):
    response = await repository.update_order(db=db, order_request=order_request, order_id=order_id)
    return response


@order_router.delete('/order/{order_id}', status_code=status.HTTP_200_OK, response_model=OrderResponse)
async def delete_order(order_id: int, repository: OrderRepository = Depends(OrderRepository),
                       db: Session = Depends(get_db)):
    response = await repository.delete_order(db=db, order_id=order_id)
    return response
