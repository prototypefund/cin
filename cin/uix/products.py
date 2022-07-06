from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder
from kivymd.uix.recyclegridlayout import MDRecycleGridLayout
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.card import MDCard
from kivy.uix.recycleview import RecycleView
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel
from kivy.uix.scrollview import ScrollView
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.core.window import Window
from kivymd.uix.behaviors import BackgroundColorBehavior


Builder.load_file('uix/products.kv')


class ProductScreen(MDScreen):
    pass


class ProductNavigationListItem(MDFlatButton):
    pass


class ProductNavigationLayout(RecycleBoxLayout):
    pass


class ProductNavigationList(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = [
            {
                'text': 'TEXT' + 'd'*x,
            } for x in range(6)]


class ProductLayout(MDRecycleGridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_resize=self.on_resize)
        Window.bind(on_maximize=self.on_resize)
        Window.bind(on_restore=self.on_resize)

    def on_resize(self, *args):
        self.cols = int(self.parent.width/(113))


class ProductGrid(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = [
            {
                'text': str(x),
            } for x in range(20)]


class ProductCard(MDCard, RoundedRectangularElevationBehavior):
    pass
