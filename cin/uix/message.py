
from kivy.lang.builder import Builder
from kivymd.uix.snackbar import Snackbar


Builder.load_file('uix/message.kv')


class Message(Snackbar):
    ...
