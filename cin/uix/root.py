"""The root module of the uix package."""
from kivy.lang.builder import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from cin.database import needs_upgrade
from cin.uix.database import DatabaseUpgrade


Builder.load_file('uix/root.kv')


class Root(MDFloatLayout):
    """The root layout of the application."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        if needs_upgrade():
            dialog = DatabaseUpgrade()
            self.add_widget(dialog)
