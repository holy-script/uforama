import os
from classes.base import BaseScreen
import pygame as pg

ufo_logo = os.path.join(os.path.dirname(__file__), '..', 'assets', 'uforama_logo.png')
yellow_btn_normal =  os.path.join(os.path.dirname(__file__), '..', 'assets', 'yellow_btn_normal.png')
yellow_btn_hover = os.path.join(os.path.dirname(__file__), '..', 'assets', 'yellow_btn_hover.png')
yellow_btn_active = os.path.join(os.path.dirname(__file__), '..', 'assets', 'yellow_btn_active.png')
red_btn_normal = os.path.join(os.path.dirname(__file__), '..', 'assets', 'red_btn_normal.png')
red_btn_hover = os.path.join(os.path.dirname(__file__), '..', 'assets', 'red_btn_hover.png')
red_btn_active = os.path.join(os.path.dirname(__file__), '..', 'assets', 'red_btn_active.png')
blue_btn_normal = os.path.join(os.path.dirname(__file__), '..', 'assets', 'blue_btn_normal.png')
blue_btn_hover = os.path.join(os.path.dirname(__file__), '..', 'assets', 'blue_btn_hover.png')
blue_btn_active = os.path.join(os.path.dirname(__file__), '..', 'assets', 'blue_btn_active.png')
blue_lbtn_normal = os.path.join(os.path.dirname(__file__), '..', 'assets', 'blue_lbtn_normal.png')
blue_lbtn_hover = os.path.join(os.path.dirname(__file__), '..', 'assets', 'blue_lbtn_hover.png')
blue_lbtn_active = os.path.join(os.path.dirname(__file__), '..', 'assets', 'blue_lbtn_active.png')

def menu(camera):
    menu = BaseScreen('Menu', 'black', 1.5)
    menu.set_camera(camera)
    menu.create(True)

    floating_ufo = menu.add_sprite(ufo_logo, menu.screen.get_rect().center)

    menu.btn_states['yellow'] = {
        'normal': pg.image.load(yellow_btn_normal).convert_alpha(),
        'hover': pg.image.load(yellow_btn_hover).convert_alpha(),
        'active': pg.image.load(yellow_btn_active).convert_alpha(),
    }

    (centerx, centery) = menu.screen.get_rect().center

    menu.create_btn('Start!', 36, 'hotpink', centerx, centery - 54, yellow_btn_normal, 'yellow')
    menu.create_btn('Options', 36, 'hotpink', centerx, centery + 18, yellow_btn_normal, 'yellow')
    menu.create_btn('Credits', 36, 'hotpink', centerx, centery + 90, yellow_btn_normal, 'yellow')
    menu.create_btn('Exit', 36, 'hotpink', centerx, centery + 162, yellow_btn_normal, 'yellow')
    menu.add_text(32, (centerx, centery + 226), "A Fast-Paced Shoot'Em Up with UFOs!", 'dodgerblue3')
    menu.add_text(32, (centerx, centery + 258), 'Developed by Palash Johri', 'dodgerblue3')
    
    setattr(menu, 'float_limit', 20)
    setattr(menu, 'float_counter', 0)
    setattr(menu, 'float_up', True)
    setattr(menu, 'float_from', floating_ufo.rect.centery)
    def effects(self):
        floating_ufo.rect.centery = self.float_from + self.float_counter
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

    (centerx, centery) = credits.screen.get_rect().center

    credits.add_text(36, (centerx, centery - 162), 'kenney.itch.io', 'sienna4')
    credits.add_text(36, (centerx, centery - 90), 'gamrets.itch.io', 'sienna4')
    credits.add_text(36, (centerx, centery - 18), 'mobilegamegraphics.itch.io', 'sienna4')
    credits.add_text(36, (centerx, centery + 54), 'void1gaming.itch.io', 'sienna4')
    credits.add_text(36, (centerx, centery + 126), 'gooseninja.itch.io', 'sienna4')
    credits.add_text(36, (centerx, centery + 198), 'gamesupply.itch.io', 'sienna4')

    def effects(self):
        self.handle_btn_clicks()
    setattr(BaseScreen, 'update', effects)

    return credits

def options(camera):
    options = BaseScreen('Options', 'slateblue2', 1)
    options.set_camera(camera)
    options.create(True)

    create_menu_btn(options)

    (centerx, centery) = options.screen.get_rect().center

    options.create_btn('MUTE SOUNDS', 36, 'black', centerx, centery - 54, blue_lbtn_normal, 'blue')
    options.create_btn('RESIZE HD/SD', 36, 'black', centerx, centery + 18, blue_lbtn_normal, 'blue')
    options.create_btn('EASY/HARD', 36, 'black', centerx, centery + 90, blue_lbtn_normal, 'blue')

    options.btn_states['blue'] = {
        'normal': pg.image.load(blue_lbtn_normal).convert_alpha(),
        'hover': pg.image.load(blue_lbtn_hover).convert_alpha(),
        'active': pg.image.load(blue_lbtn_active).convert_alpha(),
    }

    def effects(self):
        self.handle_btn_clicks()
    setattr(BaseScreen, 'update', effects)

    return options

def lvls(camera):
    lvls = BaseScreen('Levels', 'deepskyblue', 1)
    lvls.set_camera(camera)
    lvls.create(True)

    create_menu_btn(lvls)

    (centerx, centery) = lvls.screen.get_rect().center

    lvls.create_btn('1', 36, 'black', centerx, centery, blue_btn_normal, 'blue')

    lvls.btn_states['blue'] = {
        'normal': pg.image.load(blue_btn_normal).convert_alpha(),
        'hover': pg.image.load(blue_btn_hover).convert_alpha(),
        'active': pg.image.load(blue_btn_active).convert_alpha(),
    }

    def effects(self):
        self.handle_btn_clicks()
    setattr(BaseScreen, 'update', effects)

    return lvls

def create_menu_btn(screen):
    screen.btn_states['red'] = {
        'normal': pg.image.load(red_btn_normal).convert_alpha(),
        'hover': pg.image.load(red_btn_hover).convert_alpha(),
        'active': pg.image.load(red_btn_active).convert_alpha(),
    }

    (topleftx, toplefty) = screen.screen.get_rect().topleft

    screen.create_btn('Menu', 20, screen.bg, topleftx + 48, toplefty + 48, red_btn_normal, 'red')