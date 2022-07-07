"""Tests for the app module."""
from unittest.mock import patch
from cin.app import App


class TestDeviceProperty():
    """Tests for the device property."""

    def test_media_property_was_set(self):
        """The device property was set."""

        with patch('kivy.app.runTouchApp', return_value=None):
            app = App()
            app.run()
            app.device = 'S'

            assert app.device == 'S'

            app.device = 'L'

            assert app.device == 'L'


class TestUpdateMedia():
    """Tests for the _update_media method."""

    def test_update_device(self):
        """The _update_device method was called if the window size changed."""
        with patch('kivy.app.runTouchApp', return_value=None):
            app = App()
            app.run()
            app.device = 'S'

            assert app.device == 'S'

            app.root_window.size = (700, 800)

            assert app.device == 'M'

    def test_initialized_media_width(self):
        """Initial device width is used."""

        with patch('kivy.app.runTouchApp', return_value=None):
            app = App(small_device=200, medium_device=400)
            app.run()
            app.device = 'S'

            assert app.device == 'S'

            app.root_window.size = (401, 800)

            assert app.device == 'L'

            app.root_window.size = (399, 800)

            assert app.device == 'M'

            app.root_window.size = (199, 800)

            assert app.device == 'S'
