"""The module of the application main widget."""
from kivy.lang.builder import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.app import MDApp


Builder.load_file('uix/app.kv')


class App(MDBoxLayout):
    """The application layout."""

    def on_kv_post(self, widget):
        app = MDApp.get_running_app()
        app.refs['main_screen_manager'] = widget.ids.main_screen_manager


class AppBar(MDTopAppBar):
    ...


class AppNavigation(MDNavigationDrawer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_state('close')
        self._app = MDApp.get_running_app()

    def on_state(self, instance, value):
        self._app.refs['product-grid'].on_resize()
