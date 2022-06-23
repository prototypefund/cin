"""The root module of the uix package."""
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout


Builder.load_file('uix/root.kv')


class CRoot(BoxLayout):
    """The root layout of the application."""

    pass
