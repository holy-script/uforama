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

def lose(camera):
    lose = BaseScreen('Lose', 'dimgray', 1)
    lose.set_camera(camera)
    lose.create()
    (x, y) = lose.screen.get_rect().center
    lose.add_text(40, (x, y), 'MISSON FAILED :(', 'firebrick3')
    lose.evts_added = True
    return lose

def win(camera):
    win = BaseScreen('Win', 'chartreuse3', 1)
    win.set_camera(camera)
    win.create()
    (x, y) = win.screen.get_rect().center
    win.add_text(40, (x, y), 'MISSION SUCCESS :)', 'goldenrod2')
    win.evts_added = True
    return win