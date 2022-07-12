from kivy.lang.builder import Builder
from kivymd.uix.recyclegridlayout import MDRecycleGridLayout
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.card import MDCard
from kivy.uix.recycleview import RecycleView
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window
from kivymd.uix.segmentedcontrol import MDSegmentedControl


Builder.load_file('uix/products.kv')


class Products(MDBoxLayout):
    pass


class ProductNavigation(MDSegmentedControl):
    pass


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
