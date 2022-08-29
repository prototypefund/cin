from kivymd.app import MDApp
from sqlalchemy import select
from cin import models
# from cin.uix.receipt import ReceiptListItem
from copy import deepcopy
from datetime import datetime


class Sale:
    def __init__(self):
        self._app = MDApp.get_running_app()

        with self._app.db_session() as session:
            statement = select(models.Sale.id) \
                .where(models.Sale.data['state'].as_string() == 'open')
            id = session.execute(statement).scalars().first()

            if id:
                self._id = id

            else:
                sale = models.Sale(
                        data={
                            'state': 'open',
                            'opened': datetime.now().isoformat(),
                            'closed': '',
                            'sales': [],
                            'tse': {}
                            })

                session.add(sale)
                session.commit()
                self._id = sale.id

    def close(self):
        with self._app.db_session() as session:
            statement = select(models.Sale) \
                .where(models.Sale.id == self._id)
            sale = session.execute(statement).scalars().first()

            data = sale.data.copy()
            data['state'] = 'closed'
            data['closed'] = datetime.now().isoformat()
            sale.data = data
            session.commit()
            receipt = self._app.refs['receipt']
            sum = self._app.refs['sum']
            receipt.update()
            sum.update()

    def list(self):
        with self._app.db_session() as session:
            statement = select(models.Sale) \
                .where(models.Sale.id == self._id)
            sale = session.execute(statement).scalars().first()

            return sale.data['sales']

    def add(self, product_id):
        with self._app.db_session() as session:
            statement = select(models.Product) \
                .where(models.Product.id == product_id)
            product = session.execute(statement).scalars().first()

            statement = select(models.Sale) \
                .where(models.Sale.id == self._id)
            sale = session.execute(statement).scalars().first()

            sale_data = {
                    'quantity': 1,
                    'product': {
                        'name': product.data['name'],
                        'description': product.data['description'],
                        'brand': product.data['brand'],
                        'salePrice': product.data['salePrice'],
                        'tax': product.data['tax']
                        }
                    }

            data = deepcopy(sale.data)
            data['sales'].append(sale_data)
            sale.data = data
            session.commit()

            receipt = self._app.refs['receipt']
            sum = self._app.refs['sum']
            receipt.update()
            sum.update()

    def remove(self, index):
        with self._app.db_session() as session:
            statement = select(models.Sale) \
                .where(models.Sale.id == self._id)
            sale = session.execute(statement).scalars().first()

            data = deepcopy(sale.data)

            try:
                data['sales'].pop(index)
            except IndexError:
                ...

            sale.data = data
            session.commit()

    def sum(self):
        with self._app.db_session() as session:
            statement = select(models.Sale) \
                .where(models.Sale.id == self._id)
            sale = session.execute(statement).scalars().first()

            sum = .00
            for sale_data in sale.data['sales']:
                sum += sale_data['product']['salePrice']*sale_data['quantity']

        return round(sum, 2)

    def tax(self):
        with self._app.db_session() as session:
            statement = select(models.Sale) \
                .where(models.Sale.id == self._id)
            sale = session.execute(statement).scalars().first()

            taxes = {0.19: .0}
            for sale_data in sale.data['sales']:
                tax = sale_data['product']['tax']

                if tax not in taxes.keys():
                    taxes[tax] = .0

                taxes[tax] += \
                    tax*sale_data['product']['salePrice']*sale_data['quantity']

        return taxes
