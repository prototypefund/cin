"""The cin package."""
from cin.app import App


def cin() -> None:
    """Entry point for the console script cin."""
    app = App()
    app.run()
