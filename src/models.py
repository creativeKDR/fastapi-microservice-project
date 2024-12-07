from sqlalchemy import String, BIGINT, DECIMAL, Column, INTEGER
from src.db import Base


class Order(Base):
    __tablename__ = 'Order'
    id = Column(INTEGER, autoincrement=True, primary_key=True)
    product_id = Column(String(100), default=None, nullable=True)
    price = Column(DECIMAL(9, 2), nullable=False)
    total = Column(DECIMAL(9, 2), nullable=False)
    quantity = Column(DECIMAL(9, 2), nullable=False)
    status = Column(String(100), default=None, nullable=True)
