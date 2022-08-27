"""The module for database related widgets."""
from kivy.lang.builder import Builder
from kivymd.uix.card import MDCard
from kivymd.uix.behaviors.elevation import RectangularElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.app import App
from cin.database import apply_upgrade


Builder.load_file('uix/database.kv')


class DatabaseUpgradeDialog(MDBoxLayout):
    """This widget informs about a needed upgrade."""


class DatabaseUpgradeProgress(MDBoxLayout):
    """This widget shows a spinner and text during upgrade."""
    pass


class DatabaseUpgrade(MDCard, RectangularElevationBehavior):
    """A dialog that pops up when a database upgrade is needed."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._dialog = DatabaseUpgradeDialog()
        self.add_widget(self._dialog)

    def apply_upgrade(self):
        app = App.get_running_app()
        self.remove_widget(self._dialog)
        self._progress = DatabaseUpgradeProgress()
        self.add_widget(self._progress)

        def callback(arg):
            apply_upgrade(app)
            self.remove_widget(self._progress)
            app.after_db_upgrade()

        from kivy.clock import Clock
        Clock.schedule_once(callback, 1.)
