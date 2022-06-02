import os
from screens.base import BaseScreen
import pygame as pg

ufo_logo = os.path.join(os.path.dirname(__file__), '..', 'assets', 'uforama_logo.png')
btn_normal =  os.path.join(os.path.dirname(__file__), '..', 'assets', 'btn_normal.png')
btn_hover = os.path.join(os.path.dirname(__file__), '..', 'assets', 'btn_hover.png')
btn_active = os.path.join(os.path.dirname(__file__), '..', 'assets', 'btn_active.png')

def menu(camera):
    menu = BaseScreen('black', 2)
    menu.set_camera(camera)
    menu.create(True)

    floating_ufo = menu.add_sprite(ufo_logo, menu.screen.get_rect().center)

    btns = {}
    def create_btn(name, y):
        center_y = menu.screen.get_rect().centery + y
        btns[name] = {
            f'{name}_y': center_y + y,
            f'{name}_y_active': center_y + y + 2,
            f'{name}_btn': menu.add_sprite(btn_normal, menu.screen.get_rect(centery=center_y+y).center),
            f'{name}_txt': menu.add_text(36, menu.screen.get_rect(centery=center_y+y).center, name, 'hotpink')
        }
    setattr(menu, 'btns', btns)

    create_btn('Play!', -18)
    create_btn('Options', 18)
    create_btn('Credits', 54)
    create_btn('Exit', 90)
    
    setattr(menu, 'float_limit', 20)
    setattr(menu, 'float_counter', 0)
    setattr(menu, 'float_up', True)
    setattr(menu, 'float_from', floating_ufo[0].rect.centery)
    def effects(self):
        floating_ufo[0].rect.centery = self.float_from + self.float_counter
        if self.float_up:
            if self.float_counter < self.float_limit:
                self.float_counter += 0.5
            else:
                self.float_counter = self.float_limit - 1
                self.float_up = False
        else:
            if self.float_counter > 0:
                self.float_counter -= 0.5
            else:
                self.float_counter = 1
                self.float_up = True
        
        for name in self.btns:
            btn_data = self.btns[name]
            if btn_data[f'{name}_btn'][0].rect.collidepoint(pg.mouse.get_pos()):
                if pg.mouse.get_pressed()[0]:
                    self.change_btn(btn_data[f'{name}_btn'][1], 'active')
                    btn_data[f'{name}_btn'][0].rect.centery = btn_data[f'{name}_y_active']
                else:
                    self.change_btn(btn_data[f'{name}_btn'][1], 'hover')
                    btn_data[f'{name}_btn'][0].rect.centery = btn_data[f'{name}_y']
                self.change_textpos(btn_data[f'{name}_txt'][-1], btn_data[f'{name}_btn'][0].rect.center)
            else:
                self.change_btn(btn_data[f'{name}_btn'][1], 'normal')
    setattr(BaseScreen, 'update', effects)

    setattr(menu, 'menu_btn', {
        'normal': pg.image.load(btn_normal),
        'hover': pg.image.load(btn_hover),
        'active': pg.image.load(btn_active),
    })
    def change_btn(self, index, state):
        self.sprites[index].image = self.menu_btn[state]
    setattr(BaseScreen, 'change_btn', change_btn)
    def change_textpos(self, index, pos):
        self.texts[index] = (self.texts[index][0], pos)
    setattr(BaseScreen, 'change_textpos', change_textpos)
    return menu
