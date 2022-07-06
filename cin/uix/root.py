"""The root module of the uix package."""
from kivy.lang.builder import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout


Builder.load_file('uix/root.kv')


class Root(MDFloatLayout):
    """The root layout of the application."""

    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #
    #     print('root widget')
    #
    #     if needs_upgrade():
    #         self._db_upgrade = DatabaseUpgrade()
    #         self.add_widget(self._db_upgrade)
    #
    # def after_db_upgrade(self):
    #     self.remove_widget(self._db_upgrade)
    #
    #     print('finished!!!')
