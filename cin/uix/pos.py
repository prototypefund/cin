from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors import RectangularElevationBehavior
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager


Builder.load_file('uix/pos.kv')


class Sale(RectangularElevationBehavior, MDBoxLayout):
    pass


class PosScreen(MDScreen):
    pass


class ProductScreenManager(ScreenManager):
    pass
