"""The module contains the database models."""
from cin.database import Base


class Product(Base):
    """The model for product."""


class Sale(Base):
    """The model for receipt."""


class Payment(Base):
    """The model for Pyments."""
