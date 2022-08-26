"""The module contains the database models."""
from sqlalchemy import Column, String, JSON
from cin.database import Base


class Products(Base):
    """The model for product groups."""
    __tablename__ = 'products'

    id = Column(String, primary_key=True)
    data = Column(JSON)
