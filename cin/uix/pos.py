from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang.builder import Builder


Builder.load_file('uix/pos.kv')


class PosScreen(MDBoxLayout, MDScreen):
    pass
