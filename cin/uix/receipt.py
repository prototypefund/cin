from kivymd.uix.datatables import MDDataTable
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang.builder import Builder
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.metrics import dp
from kivy.uix.recycleview import RecycleView
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivymd.uix.behaviors import BackgroundColorBehavior


Builder.load_file('uix/receipt.kv')


class ReceiptListItem(MDBoxLayout, BackgroundColorBehavior):
    pass


class Receipt(RecycleView, BackgroundColorBehavior):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = [
            {
                'number': str(x),
                'product': f'Product{x}',
                'quantity': str(1),
                'price': str(2.45)
            } for x in range(10)]
