import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App as KVApp
from kivy.uix.label import Label


class App(KVApp):
    def build(self):
        return Label(text='CIN app')
