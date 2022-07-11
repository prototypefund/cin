"""The module of the application main widget."""
from kivy.lang.builder import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.navigationrail import MDNavigationRail
from kivymd.uix.navigationdrawer import MDNavigationDrawer


Builder.load_file('uix/app.kv')


class App(MDBoxLayout):
    """The application layout."""


class AppBar(MDTopAppBar):
    pass


class AppNavigation(MDNavigationDrawer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_state('open')
