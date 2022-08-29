from kivymd.app import MDApp
from sqlalchemy import select
from cin import models


class Sale:
    def __init__(self):
        self._app = MDApp.get_running_app()

        with self._app.db_session() as session:
            statement = select(models.Sale) \
                .where(models.Sale.data['state'].as_string() == 'open')
            result = session.execute(statement).scalars().first()

            print(result)

            if result:
                self._sale = result

            else:
                self._sale = models.Sale(
                        data={
                            'state': 'open',
                            'products': [],
                            'tse': {}
                            })

                session.add(self._sale)
                session.commit()

    def close(self):
        with self._app.db_session() as session:
            session.add(self._sale)
            data = self._sale.data.copy()
            data['state'] = 'closed'
            self._sale.data = data
            session.commit()
