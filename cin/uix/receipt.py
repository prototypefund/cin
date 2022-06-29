from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang.builder import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivymd.uix.behaviors import BackgroundColorBehavior


Builder.load_file('uix/receipt.kv')


class ReceiptListItem(MDBoxLayout, BackgroundColorBehavior):
    pass


class ReceiptLayout(BackgroundColorBehavior, RecycleBoxLayout):
    pass


class ReceiptList(RecycleView, BackgroundColorBehavior):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = [
            {
                'number': str(x),
                'product': f'Product{x}',
                'quantity': str(1),
                'price': str(2.45)
            } for x in range(10)]


class Receipt(MDBoxLayout):
    pass
