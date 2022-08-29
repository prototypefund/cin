from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang.builder import Builder
from kivymd.uix.list import TwoLineAvatarIconListItem, IRightBodyTouch, ILeftBodyTouch
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivymd.uix.list import MDList
from kivymd.app import MDApp
from cin.transactions import Sale


Builder.load_file('uix/receipt.kv')


class ReceiptList(MDList):
    ...


class ReceiptListItem(TwoLineAvatarIconListItem):
    name = StringProperty()
    brand = StringProperty()
    price = StringProperty()


class ReceiptPrice(IRightBodyTouch, MDBoxLayout):
    adaptive_width = True


class ReceiptActions(ILeftBodyTouch, MDBoxLayout):
    adaptive_width = True


class Receipt(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._app = MDApp.get_running_app()
        self._app.refs['receipt'] = self

    def update(self):
        sale = Sale()
        receipt_list = self.ids.list
        receipt_list.clear_widgets()

        for sales in sale.list():
            receipt_list.add_widget(
                ReceiptListItem(
                    name=sales['product']['name'],
                    brand=sales['product']['brand'],
                    price=str(sales['product']['salePrice']).replace('.', ',')
                ))
