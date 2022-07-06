from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer
from alembic import command
from alembic.config import Config


class Base:
    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)


def needs_upgrade():
    return True


def apply_upgrade(app):
    db_url = app.config['database']['url']
    alembic_cfg = Config()
    alembic_cfg.set_main_option('script_location', 'cin:alembic')
    alembic_cfg.set_main_option('sqlalchemy.url', db_url)
    command.upgrade(alembic_cfg, "head")
