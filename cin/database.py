"""The module for database handling."""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer
from alembic import command
from alembic.config import Config


class Base:
    """The Base class for all ORM models."""
    id = Column(Integer, primary_key=True)
    """The primary key for all Models:"""


Base = declarative_base(cls=Base)


def needs_upgrade():
    return True


def apply_upgrade(app):
    """
    Apply a database upgrade.

    Args:
        app: The running app instance.
    """
    db_url = app.config['database']['url']
    alembic_cfg = Config()
    alembic_cfg.set_main_option('script_location', 'cin:alembic')
    alembic_cfg.set_main_option('sqlalchemy.url', db_url)
    command.upgrade(alembic_cfg, "head")
