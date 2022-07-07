"""The module for database handling."""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer
from alembic import command
from alembic.config import Config
from alembic.migration import MigrationContext
from alembic.script import ScriptDirectory
from alembic.runtime.environment import EnvironmentContext
from sqlalchemy import MetaData


meta = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    }
)
"""The SQLAlchemy naming convention."""


class Base:
    """The Base class for all ORM models."""
    id = Column(Integer, primary_key=True)
    """The primary key for all Models:"""


Base = declarative_base(cls=Base, metadata=meta)


def needs_upgrade(app):
    """
    Is database upgrade needed.

    Args:
        app: The running app instance.
    """
    db_url = app.config['database']['url']
    alembic_cfg = Config()
    alembic_cfg.set_main_option('script_location', 'cin:alembic')
    alembic_cfg.set_main_option('sqlalchemy.url', db_url)
    connection = app.db_engine.connect()
    script = ScriptDirectory.from_config(alembic_cfg)
    head = EnvironmentContext(alembic_cfg, script).get_head_revision()
    context = MigrationContext.configure(connection)
    current_rev = context.get_current_revision()

    if current_rev == head:
        return False

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
    command.upgrade(alembic_cfg, 'head')
