"""The module of the application main widget."""
from kivy.lang.builder import Builder
from kivymd.uix.boxlayout import MDBoxLayout


Builder.load_file('uix/app.kv')


class App(MDBoxLayout):
    """The application layout."""
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
