import os
from classes.base import BaseScreen

pg_logo = os.path.join(os.path.dirname(__file__), '..', 'assets', 'pygame_logo.png')

def logos(camera):
    logos = BaseScreen('Logos', 'orange', 1)
    logos.set_camera(camera)
    logos.create()
    logos.add_sprite(pg_logo, logos.screen.get_rect().center)
    return logos

def banner(camera):
    banner = BaseScreen('Banner', 'pink', 1)
    banner.set_camera(camera)
    banner.create()
    (x, y) = banner.screen.get_rect().center
    banner.add_text(36, (x, y - 36), '-rama', 'black')
    banner.add_text(36, (x, y), 'noun suffix:', 'black')
    banner.add_text(36, (x, y + 36), ' meaning "sight, view, spectacular display or instance of,"', 'black')
    return banner