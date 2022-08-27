"""The module for database synchronization."""
from kivy.network.urlrequest import UrlRequest
from sqlalchemy import select
from cin.models import Product


def products(app):
    def update_db(req, data):

        with app.db_session() as session:
            statement = select(Product)
            results = session.execute(statement).scalars().all()

            for result in results:
                session.delete(result)

            session.commit()

            for product in data:
                session.add(Product(data=product))

            session.commit()

    UrlRequest('http://127.0.0.1:8000/app/products', update_db)
    # req.wait()
