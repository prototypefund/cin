from cin import config  # noqa: F401
from kivymd.app import MDApp
from cin.uix.root import Root


class App(MDApp):
    def build(self):
        """
        Initialize the application.

        It will be called only once. If this method returns a widget (tree), it
        will be used as the root widget and added to the window.
        """
        self.theme_cls.primary_palette = 'Brown'

        return Root()
