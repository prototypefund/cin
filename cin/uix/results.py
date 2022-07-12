from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

Builder.load_file('uix/results.kv')


class ResultTable(MDFloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.table = MDDataTable(
            size_hint=(0.95, 0.95),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            use_pagination=True,
            check=True,
            column_data=[
                ("No.", dp(30)),
                ("Group", dp(30)),
                ("Product", dp(60)),
                ("Price", dp(30)),
            ],
            row_data=[
                (
                    "1",
                    "Test group\ndsdsdsds",
                    "Test product\nsdsdsd\ndsdsdsdsds",
                    "12,45",
                ),
            ],
            elevation=0,
        )

        self.add_widget(self.table)


class Result(MDScreen):
    pass
