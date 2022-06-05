import os
from screens.base import BaseScreen
import pygame as pg
from pygame.locals import *

crosshair_icon = os.path.join(os.path.dirname(__file__), '..', 'assets', 'crosshair_icon.png')
ufo_green = os.path.join(os.path.dirname(__file__), '..', 'assets', 'ufo_green.png')
bg_00 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'bg_00.png')
bg_01 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'bg_01.png')
bg_02 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'bg_02.png')
bg_03 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'bg_03.png')


def play(camera, lvl):
    play = BaseScreen('Play', 'black', 1)
    play.set_camera(camera)
    play.create(True)
    play.camera.mouse.image = pg.image.load(crosshair_icon)
    play.to_copy = True

    levels = {
        '1': level1
    }

    setattr(play, 'level', lvl)
    controls = levels[str(lvl)](play)

    def effects(self):
        self.pressed = pg.key.get_pressed()
        controls(self)
    setattr(BaseScreen, 'update', effects)
    return play

def level1(screen):
    layer1 = screen.add_sprite(bg_00, (0, 0), "topleft")[0]
    (x, y) = screen.screen.get_rect().center
    (player, player_i) = screen.add_sprite(ufo_green, (x, y))
    screen.camera.player_index = player_i
    speed = 10
    setattr(screen, 'max_y', layer1.rect.bottom - player.image.get_height() * 0.1)
    setattr(screen, 'min_y', layer1.rect.top + player.image.get_height() * 0.1)
    setattr(screen, 'max_x', layer1.rect.right - player.image.get_width() * 0.1)
    setattr(screen, 'min_x', layer1.rect.left + player.image.get_width() * 0.1)

    setattr(screen, 'direction', pg.math.Vector2())

    def controls(self):
        if self.pressed[K_w]:
            self.direction.y = -1
        elif self.pressed[K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        
        if self.pressed[K_d]:
            self.direction.x = 1
        elif self.pressed[K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        
        player.rect.center += self.direction * speed
        (self.camera.player_x, self.camera.player_y) = player.rect.center
    
    return controls