import os
from screens.base import BaseScreen

def splash_screen(dimensions):
    splash = BaseScreen(dimensions, 'orchid1', 2)
    splash.create()
    splash.add_sprite(os.path.join(os.path.dirname(__file__), '..', 'assets', 'pygame_logo.png'))
    return splash