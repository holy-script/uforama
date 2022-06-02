import os
from screens.base import BaseScreen

ufo_logo = os.path.join(os.path.dirname(__file__), '..', 'assets', 'uforama_logo.png')

def menu(camera):
    menu = BaseScreen('black', 2)
    menu.set_camera(camera)
    menu.create(True)
    floating_ufo = menu.add_sprite(ufo_logo, menu.screen.get_rect().center)
    setattr(menu, 'float_limit', 20)
    setattr(menu, 'float_counter', 0)
    setattr(menu, 'float_up', True)
    setattr(menu, 'float_from', floating_ufo.rect.centery)
    def effects(self):
        floating_ufo.rect.centery = self.float_from + self.float_counter
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

    setattr(BaseScreen, 'update', effects)
    return menu
