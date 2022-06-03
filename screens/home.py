import os
from screens.base import BaseScreen
import pygame as pg

ufo_logo = os.path.join(os.path.dirname(__file__), '..', 'assets', 'uforama_logo.png')
yellow_btn_normal =  os.path.join(os.path.dirname(__file__), '..', 'assets', 'yellow_btn_normal.png')
yellow_btn_hover = os.path.join(os.path.dirname(__file__), '..', 'assets', 'yellow_btn_hover.png')
yellow_btn_active = os.path.join(os.path.dirname(__file__), '..', 'assets', 'yellow_btn_active.png')
red_btn_normal = os.path.join(os.path.dirname(__file__), '..', 'assets', 'red_btn_normal.png')
red_btn_hover = os.path.join(os.path.dirname(__file__), '..', 'assets', 'red_btn_hover.png')
red_btn_active = os.path.join(os.path.dirname(__file__), '..', 'assets', 'red_btn_active.png')

def menu(camera):
    menu = BaseScreen('Menu', 'black', 1.5)
    menu.set_camera(camera)
    menu.create(True)

    floating_ufo = menu.add_sprite(ufo_logo, menu.screen.get_rect().center)

    menu.btn_states = {
        'normal': pg.image.load(yellow_btn_normal),
        'hover': pg.image.load(yellow_btn_hover),
        'active': pg.image.load(yellow_btn_active),
    }

    (centerx, centery) = menu.screen.get_rect().center

    menu.create_btn('Play!', 36, 'hotpink', centerx, centery - 54, yellow_btn_normal)
    menu.create_btn('Options', 36, 'hotpink', centerx, centery + 18, yellow_btn_normal)
    menu.create_btn('Credits', 36, 'hotpink', centerx, centery + 90, yellow_btn_normal)
    menu.create_btn('Exit', 36, 'hotpink', centerx, centery + 162, yellow_btn_normal)
    
    setattr(menu, 'float_limit', 20)
    setattr(menu, 'float_counter', 0)
    setattr(menu, 'float_up', True)
    setattr(menu, 'float_from', floating_ufo[0].rect.centery)
    def effects(self):
        floating_ufo[0].rect.centery = self.float_from + self.float_counter
        if self.float_up:
            if self.float_counter < self.float_limit:
                self.float_counter += 1
            else:
                self.float_counter = self.float_limit - 1
                self.float_up = False
        else:
            if self.float_counter > 0:
                self.float_counter -= 1
            else:
                self.float_counter = 1
                self.float_up = True
        
        self.handle_btn_clicks()
    setattr(BaseScreen, 'update', effects)

    return menu


def credits(camera):
    credits = BaseScreen('Credits', 'seagreen1', 1)
    credits.set_camera(camera)
    credits.create(True)

    create_menu_btn(credits)

    def effects(self):
        self.handle_btn_clicks()
    setattr(BaseScreen, 'update', effects)

    return credits

def options(camera):
    options = BaseScreen('Options', 'slateblue2', 1)
    options.set_camera(camera)
    options.create(True)

    create_menu_btn(options)

    def effects(self):
        self.handle_btn_clicks()
    setattr(BaseScreen, 'update', effects)

    return options

def lvls(camera):
    lvls = BaseScreen('Levels', 'deepskyblue', 1)
    lvls.set_camera(camera)
    lvls.create(True)

    create_menu_btn(lvls)

    def effects(self):
        self.handle_btn_clicks()
    setattr(BaseScreen, 'update', effects)

    return lvls

def create_menu_btn(screen):
    screen.btn_states = {
        'normal': pg.image.load(red_btn_normal),
        'hover': pg.image.load(red_btn_hover),
        'active': pg.image.load(red_btn_active),
    }

    (topleftx, toplefty) = screen.screen.get_rect().topleft

    screen.create_btn('Menu', 20, 'black', topleftx + 48, toplefty + 48, red_btn_normal)