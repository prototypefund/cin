from xix import app
from kivy.uix.label import Label


class App(app.App):
    def build(self):
        return Label(text='CIN-POS app')
