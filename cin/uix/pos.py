from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder
from kivymd.app import MDApp


Builder.load_file('uix/pos.kv')


class Pos(MDScreen):
    ...


class PosScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_kv_post(self, widget):
        app = MDApp.get_running_app()
        app.refs['pos_screen_manager'] = self.ids.pos_screen_manager
