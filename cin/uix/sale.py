from kivy.lang.builder import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton, MDIconButton, MDRectangleFlatIconButton
from kivymd.uix.behaviors import RectangularElevationBehavior


Builder.load_file('uix/sale.kv')


class Sale(MDBoxLayout, RectangularElevationBehavior):
    pass


class NumberButton(MDRectangleFlatIconButton):
    pass


class NumberActionButton(MDRectangleFlatIconButton):
    pass
