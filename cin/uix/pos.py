from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors import RectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabs, MDTabsBase
from kivy.clock import Clock
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from cin.uix.products import Products
from cin.uix.sale import Sale


Builder.load_file('uix/pos.kv')


class PosLayoutSmall(MDTabs):
    pass


class PosLayoutDefault(MDBoxLayout):
    pass


class PosTabSmall(MDBoxLayout, MDTabsBase):
    pass


class Pos(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        app = MDApp.get_running_app()
        app.bind(device=self.on_device)
        self._layout_small = PosLayoutSmall()
        self._products_tab_small = PosTabSmall(title='Products')
        self._sale_tab_small = PosTabSmall(title='Sale')
        self._layout_small.add_widget(self._products_tab_small)
        self._layout_small.add_widget(self._sale_tab_small)
        self._layout_default = PosLayoutDefault()
        self._sale = Sale()
        self._products = Products()

    def on_device(self, instance, value):
        if value == 'S':
            if self._layout_small not in self.children:
                if self._layout_default in self.children:
                    self._layout_default.remove_widget(self._products)
                    self._layout_default.remove_widget(self._sale)
                    self.remove_widget(self._layout_default)

                self._products_tab_small.add_widget(self._products)
                self._sale_tab_small.add_widget(self._sale)
                self.add_widget(self._layout_small)

        else:
            if self._layout_default not in self.children:
                if self._layout_small in self.children:
                    self._products_tab_small.remove_widget(self._products)
                    self._sale_tab_small.remove_widget(self._sale)
                    self.remove_widget(self._layout_small)

                self._layout_default.add_widget(self._products)
                self._layout_default.add_widget(self._sale)
                self.add_widget(self._layout_default)

    # def on_device(self, instance, value):
    #     if value == 'S':
    #         if self._layout_default:
    #             self._layout_default.remove_widget(self._products)
    #             self._layout_default.remove_widget(self._sale)
    #             self.remove_widget(self._layout_default)
    #
    #         if not self._layout_small:
    #             self._layout_small = PosLayoutSmall()
    #             self._products_tab = PosTabSmall(title='Products')
    #             self._products_tab.add_widget(self._products)
    #             self._sale_tab = PosTabSmall(title='Sale')
    #             self._sale_tab.add_widget(self._sale)
    #
    #         self._layout_small.add_widget(self._products_tab)
    #         self._layout_small.add_widget(self._sale_tab)
    #         self.add_widget(self._layout_small)
    #
    #     else:
    #         if self._layout_small:
    #             self._products_tab.remove_widget(self._products)
    #             self._sale_tab.remove_widget(self._sale)
    #             self.remove_widget(self._layout_small)
    #
    #         if not self._layout_default:
    #             self._layout_default = PosLayoutDefault()
    #
    #         self._layout_default.add_widget(self._products)
    #         self._layout_default.add_widget(self._sale)
    #         self.add_widget(self._layout_default)


class PosScreen(MDScreen, ScreenManager):
    pass
