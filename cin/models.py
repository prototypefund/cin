"""The module contains the database models."""
from sqlalchemy import Column, Integer, JSON
from cin.database import Base


class Product(Base):
    """The model for product groups."""
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(JSON)
