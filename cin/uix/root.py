"""The root module of the uix package."""
from kivy.lang.builder import Builder
from kivymd.uix.boxlayout import MDBoxLayout


Builder.load_file('uix/root.kv')


class Root(MDBoxLayout):
    """The root layout of the application."""

    pass
