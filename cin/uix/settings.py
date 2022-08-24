from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.behaviors import RectangularElevationBehavior
from kivymd.uix.card import MDCard
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.selectioncontrol import MDSwitch
from kivy.app import App
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.filemanager import MDFileManager
from pathlib import Path


Builder.load_file('uix/settings.kv')


class SettingsCard(MDCard, RectangularElevationBehavior):
    ...


class SettingsScreen(MDScreen):
    pass


class Tse(MDScrollView, MDTabsBase):
    ...


class TseEnableSwitch(MDSwitch):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._app = App.get_running_app()
        self.active = eval(self._app.config['tse']['enabled'])

    def on_active(self, instance, value):
        super().on_active(instance, value)
        self._app.config['tse']['enabled'] = str(value)


class TseClientNameField(MDTextField):
    def on_text(self, instance, value):
        app = App.get_running_app()
        app.config['tse']['client_name'] = value


class TseHostField(MDTextField):
    def on_text(self, instance, value):
        app = App.get_running_app()
        app.config['tse']['host'] = value


class TseFullExportButton(MDRaisedButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._path = None

    def on_release(self):
        self._file_manager = MDFileManager(
                selector='folder',
                exit_manager=self.exit_manager,
                select_path=self.select_path)
        self._file_manager.show(str(Path.home()))

    def select_path(self, path):
        self._path = path
        self.exit_manager()

    def exit_manager(self, *args):
        self._path = None
        self._file_manager.close()


class Profile(MDTabsBase):
    ...
