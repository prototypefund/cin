from kivy.app import App as KVApp
from kivy.uix.label import Label


class App(KVApp):
    def build(self):
        return Label(text='CIN-POS app')
