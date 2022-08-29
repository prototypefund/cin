from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang.builder import Builder
from kivymd.uix.list import TwoLineAvatarIconListItem, IRightBodyTouch, ILeftBodyTouch
from kivy.uix.scrollview import ScrollView


Builder.load_file('uix/receipt.kv')


class ReceiptListItem(TwoLineAvatarIconListItem):
    pass


class ReceiptPrice(IRightBodyTouch, MDBoxLayout):
    adaptive_width = True


class ReceiptActions(ILeftBodyTouch, MDBoxLayout):
    adaptive_width = True


class Receipt(ScrollView):
    pass
