from cin import config  # noqa: F401
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from kivy.animation import Animation
from kivy.properties import OptionProperty
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.metrics import dp
from cin.database import needs_upgrade
from cin.uix.database import DatabaseUpgrade
from cin.uix.app import App as AppWidget


class Root(MDScreen):
    """The root layout of the application."""


class App(MDApp):
    device = OptionProperty('S', options=('S', 'M', 'L'))
    """The media property (The possible values are S, M and L)"""
    use_kivy_settings = False

    def __init__(
            self,
            small_device: str = 470,
            medium_device: str = 1200,
            **kwargs: int
            ) -> None:
        """Initialize the App class instance."""
        super().__init__(**kwargs)
        self._small_device = dp(small_device)
        self._medium_device = dp(medium_device)
        self.refs = {}
        Window.bind(on_resize=self._update_device)

    def _add_app_widget(self) -> None:
        """Add the applications root widget."""
        from cin.uix import settings
        self.app = settings.SettingsScreen()
        # self.app = AppWidget(opacity=.0)
        self.root.add_widget(self.app)
        animation = Animation(opacity=1., duration=1., t='in_out_sine')
        animation.start(self.app)

    def _update_device(self, window: Window, width: int, height: int) -> None:
        """
        Update the device property.

        This is an internal callback that responds to the resize event of
        the window and sets the media property accordingly.

        Args:
            window: The application window.
            width: The new width.
            height: The new window height.
        """
        self.device = (
            'S' if width < self._small_device else
            'M' if width < self._medium_device else
            'L'
        )

    def build(self) -> None:
        """
        Initialize the application.

        It will be called only once. If this method returns a widget (tree), it
        will be used as the root widget and added to the window.
        """
        self.title = 'cin'
        Window.clearcolor = (1, 1, 1, 1)
        self.theme_cls.primary_palette = 'Brown'

        return Root()

    def build_config(self, config) -> None:
        """Build the initial config file."""
        config.setdefaults('cin', {
            'db_url': f'sqlite:///{self.data_dir/"cin.db"}',
            'tse_enabled': False
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
        db_url = self.config['cin']['db_url']
        self.db_engine = create_engine(db_url)
        self.db_session = sessionmaker(self.db_engine)

        if needs_upgrade(self):
            self._db_upgrade = DatabaseUpgrade()
            self.root.add_widget(self._db_upgrade)
        else:
            self._add_app_widget()

    def after_db_upgrade(self):
        self.root.remove_widget(self._db_upgrade)
        self._add_app_widget()
