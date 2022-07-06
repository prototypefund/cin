"""The module for database related widgets."""
from kivy.lang.builder import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDFlatButton, MDRaisedButton

Builder.load_file('uix/database.kv')


class DatabaseUpgrade(MDCard):
    """A dialog that pops up when a database upgrade is needed."""
