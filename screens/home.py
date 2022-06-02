import os
from screens.base import BaseScreen

def menu(camera):
    menu = BaseScreen('lightblue', 2)
    menu.set_camera(camera)
    menu.create()
    return menu
