from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer


class Base:
    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)


def needs_upgrade():
    return True
