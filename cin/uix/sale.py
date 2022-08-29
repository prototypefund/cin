from kivy.lang.builder import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import (
        MDRaisedButton, MDFlatButton, MDRectangleFlatIconButton)
from kivymd.uix.behaviors import RectangularElevationBehavior
from kivymd.uix.textfield import MDTextField
from kivy.properties import NumericProperty
from kivymd.app import MDApp
from cin import transactions
from kivymd.uix.dialog import MDDialog
from cin import transactions


Builder.load_file('uix/sale.kv')


class Sale(MDBoxLayout, RectangularElevationBehavior):
    pass


class CashContent(MDBoxLayout):
    ...


class DialogCard(MDCard, RectangularElevationBehavior):
    pass


class PayDialog(MDDialog):
    def __init__(self, **kwargs):
        self.buttons = [
            MDFlatButton(text='ABBRECHEN'),
            MDRaisedButton(text='BEZAHLT')
        ]
        super().__init__(**kwargs)


class CashPayDialog(PayDialog):
    def __init__(self, **kwargs):
        self.content_cls = CashContent()
        super().__init__(**kwargs)


class NumberButton(MDRectangleFlatIconButton):
    pass


class PayNumberButton(NumberButton):
    def on_release(self):
        given_cash = self.parent.parent.ids.given_cash
        given_cash.text = given_cash.text + self.text


class NumberActionButton(MDRectangleFlatIconButton):
    ...


class GivenCashField(MDTextField):
    value = NumericProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.vaule = 0.0

    def on_text(self, instance, value):
        to_pay = self.parent.parent.ids.to_pay.value
        return_cash = self.parent.parent.ids.return_cash

        self.value = float(self.text.replace(',', '.'))
        return_cash.value = self.value-to_pay


class CashButton(NumberActionButton):
    def on_release(self):
        dialog = CashPayDialog()
        dialog.open()


class ToPayLabel(MDLabel):
    value = NumericProperty()

    def on_kv_post(self, widget):
        self.value = transactions.Sale().sum()
        self.text = str(round(self.value, 2)).replace('.', ',') + '€'


class ReturnCash(MDLabel):
    value = NumericProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.vaule = 0.0

    def on_value(self, instance, value):
        self.text = str(round(value, 2)).replace('.', ',') + '€'


class Sum(MDLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._app = MDApp.get_running_app()
        self._app.refs['sum'] = self

    def update(self):
        sale = transactions.Sale()
        self.text = str(round(sale.sum(), 2)).replace('.', ',') + '€'
