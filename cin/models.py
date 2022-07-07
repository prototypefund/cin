"""The module contains the database models."""
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from cin.database import Base


class ProductGroup(Base):
    """The model for product groups."""
    __tablename__ = 'product_groups'

    group_id = Column(String, unique=True, nullable=False)
    parent_id = Column(String, ForeignKey('product_groups.group_id'))
    name = Column(String, nullable=False)
    description = Column(String)
    children = relationship('ProductGroup')
