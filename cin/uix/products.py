from kivy.lang.builder import Builder
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.core.window import Window
from kivymd.uix.segmentedcontrol import MDSegmentedControl
from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivy.properties import StringProperty
from cin.models import Product
from kivymd.uix.dialog import MDDialog
from sqlalchemy import select
from pathlib import Path


Builder.load_file('uix/products.kv')


class Products(MDBoxLayout):
    ...


class ProductNavigation(MDSegmentedControl):
    ...


class ProductInfo(MDBoxLayout):
    name = StringProperty()
    brand = StringProperty()
    description = StringProperty()
    price = StringProperty()
    sale_price = StringProperty()
    tax = StringProperty()
    ean_code = StringProperty()


class ProductCard(MDCard, RoundedRectangularElevationBehavior):
    name = StringProperty()
    price = StringProperty()
    image = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ProductGrid(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_resize=self.on_resize)
        Window.bind(on_maximize=self.on_resize)
        Window.bind(on_restore=self.on_resize)
        Window.bind(on_restore=self.on_resize)
        self._app = MDApp.get_running_app()
        self._app.refs['product-grid'] = self

    def on_resize(self, *args):
        self.ids.grid.cols = int(self.width/(220))

    def update(self):
        with self._app.db_session() as session:
            statement = select(Product)
            results = session.execute(statement).scalars().all()

            for result in results:
                name = result.data['name']
                sale_price = str(result.data['salePrice']).replace('.', ',')+'€'
                image_name = Path(result.data['imageLink']).name
                image_path = Path(self._app.data_dir/'products/images'/image_name)

                product = ProductCard(
                        name=name,
                        price=sale_price,
                        image=str(image_path))

                product.info = MDDialog(
                        title='Produktinformation',
                        content_cls=ProductInfo(
                            name=name,
                            brand=result.data['brand'],
                            description=result.data['description'],
                            price=str(result.data['price']).replace('.', ',')+'€',
                            sale_price=sale_price,
                            tax=str(result.data['tax']*100).replace('.', ',')+'%',
                            ean_code=result.data['eanCode'],
                            ),
                        type='custom')

                self.ids.grid.add_widget(product)

    def on_kv_post(self, instance):
        self.update()
