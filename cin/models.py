"""The module contains the database models."""
from sqlalchemy import Column, JSON
from cin.database import Base


class ProductGroup(Base):
    """The model for product groups."""
    __tablename__ = 'product_groups'

    data = Column(JSON)
