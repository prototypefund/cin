from cin import config  # noqa: F401
from kivymd.app import MDApp
from cin.uix.root import Root
from kivy.core.window import Window
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alembic import command
from alembic.config import Config
from cin.database import Base


class App(MDApp):
    def build(self):
        """
        Initialize the application.

        It will be called only once. If this method returns a widget (tree), it
        will be used as the root widget and added to the window.
        """
        self.title = 'cin'
        Window.clearcolor = (1, 1, 1, 1)
        self.theme_cls.primary_palette = 'Brown'

        return Root()

    def build_config(self, config):
        config.setdefaults('database', {
            'url': f'sqlite:///{self.data_dir/"cin.db"}'
        })

    @property
    def data_dir(self):
        path = Path(self.user_data_dir)/'cin'
        path.mkdir(parents=True, exist_ok=True)

        return path

    def get_application_config(self):
        path = self.data_dir/'settings.ini'

        return super().get_application_config(path)

    def on_start(self):
        db_url = self.config['database']['url']
        alembic_cfg = Config()
        alembic_cfg.set_main_option('script_location', 'cin:alembic')
        alembic_cfg.set_main_option('sqlalchemy.url', db_url)
        command.upgrade(alembic_cfg, "head")
        # self.db_engine = create_engine(db_url, echo=True, future=True)
        # self.db_session = sessionmaker(self.db_engine)
