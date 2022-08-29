"""The module for database synchronization."""
from kivy.network.urlrequest import UrlRequest
from sqlalchemy import select
from cin.models import Product
from cin.uix.message import Message
from pathlib import Path
import shutil


def products(app):
    url = app.config.get('backend', 'url')

    if url.endswith('/'):
        url = url.rstrip('/')

    def update_db(req, data):
        with app.db_session() as session:
            message = Message(
                text='Die Produkt werder mit dem Server synchronisiert.',
                auto_dismiss=True)

            message.open()
            statement = select(Product)
            results = session.execute(statement).scalars().all()

            for result in results:
                session.delete(result)

            session.commit()

            images_path = app.data_dir/'products/images'
            shutil.rmtree(images_path, ignore_errors=True)
            images_path.mkdir(parents=True, exist_ok=True)

            for product in data:
                session.add(Product(data=product))

                url_path = Path(product['imageLink'])
                image_file = images_path/url_path.name

                UrlRequest(
                        url + '/' + product['imageLink'],
                        file_path=image_file)

            session.commit()

    def on_error(req, error):
        message = Message(
            text='[color=#C70039]Das Server ist nicht erreichbar![/color]',
            auto_dismiss=True)

        message.open()

    UrlRequest(url + '/app/products', on_success=update_db, on_error=on_error)
