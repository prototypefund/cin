"""The module contains the database models."""
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from cin.database import Base


class Category(Base):
    """The model for product groups."""
    __tablename__ = 'category'

    id = Column(String, primary_key=True)
    parent_id = Column(String, ForeignKey('category.id'))
    name = Column(String, nullable=False)
    description = Column(String)
    children = relationship('Category')
