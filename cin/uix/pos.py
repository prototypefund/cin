from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder
from kivymd.app import MDApp
from cin import sync
from cin.uix.message import Message


Builder.load_file('uix/pos.kv')


class Pos(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._app = MDApp.get_running_app()

        # message = Message(
        #     text='Die Produkt werder mit dem Server synchronisiert.',
        #     auto_dismiss=True)
        #
        # message.open()

        sync.products(self._app)

class PosScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_kv_post(self, widget):
        app = MDApp.get_running_app()
        app.refs['pos_screen_manager'] = self.ids.pos_screen_manager
