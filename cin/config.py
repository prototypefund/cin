"""The config module."""
from pathlib import Path
from kivy.config import Config
from kivy.resources import resource_add_path


resource_add_path(Path(__file__).parent.absolute())

Config.set('graphics', 'minimum_width', 300)
Config.set('graphics', 'minimum_height', 400)
