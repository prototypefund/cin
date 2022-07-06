from cin import config  # noqa: F401
from kivymd.app import MDApp
from kivy.core.window import Window
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from kivy.animation import Animation
from cin.database import needs_upgrade
from cin.uix.database import DatabaseUpgrade
from cin.uix.app import App as AppWidget
from kivymd.uix.floatlayout import MDFloatLayout


class Root(MDFloatLayout):
    """The root layout of the application."""


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
        if needs_upgrade():
            self._db_upgrade = DatabaseUpgrade()
            self.root.add_widget(self._db_upgrade)

    def after_db_upgrade(self):
        self.root.remove_widget(self._db_upgrade)
        app_widget = AppWidget(opacity=.0)
        self.root.add_widget(app_widget)
        animation = Animation(opacity=1., duration=1., t='in_out_sine')
        animation.start(app_widget)
