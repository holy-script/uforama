import os
from random import randint
from screens.base import BaseScreen
import pygame as pg
from pygame.locals import *

crosshair_icon = os.path.join(os.path.dirname(__file__), '..', 'assets', 'crosshair_icon.png')
ufo_green = os.path.join(os.path.dirname(__file__), '..', 'assets', 'ufo_green.png')
bg_00 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'bg_00.png')
bg_01 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'bg_01.png')
bg_02 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'bg_02.png')
bg_03 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'bg_03.png')
tree_01 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'tree_01.png')
tree_02 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'tree_02.png')
tree_03 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'tree_03.png')
tree_04 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'tree_04.png')
tree_05 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'tree_05.png')
tree_06 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'tree_06.png')
tree_07 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'tree_07.png')
tree_08 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'tree_08.png')
tree_09 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'tree_09.png')
flora_01 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'flora_01.png')
flora_02 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'flora_02.png')
flora_03 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'flora_03.png')
flora_04 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'flora_04.png')

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

    layer2_a = screen.add_sprite(bg_01, (0, layer1.rect.centery), "center")[0]
    layer2_b = screen.add_sprite(bg_01, (layer1.rect.centerx * 2, layer1.rect.centery), "center")[0]
    cloud_speed = 1

    screen.add_sprite(bg_03, (0, 1200), "bottomleft")

    screen.add_sprite(tree_04, (-6, 1010), "bottomleft")
    screen.add_sprite(tree_07, (118, 1010), "bottomleft")
    screen.add_sprite(tree_07, (234, 1010), "bottomleft")
    screen.add_sprite(tree_07, (550, 1010), "bottomleft")
    screen.add_sprite(tree_07, (688, 1010), "bottomleft")
    screen.add_sprite(tree_07, (790, 1010), "bottomleft")
    screen.add_sprite(tree_07, (1300, 1010), "bottomleft")
    screen.add_sprite(tree_07, (1424, 1010), "bottomleft")
    screen.add_sprite(tree_07, (1784, 1010), "bottomleft")
    screen.add_sprite(tree_09, (394, 1010), "bottomleft")
    screen.add_sprite(tree_02, (991, 1010), "bottomleft")
    screen.add_sprite(tree_06, (1560, 1010), "bottomleft")

    screen.add_sprite(flora_02, (1171, 1010), "bottomleft")
    screen.add_sprite(flora_01, (35, 1010), "bottomleft")
    screen.add_sprite(flora_01, (995, 1010), "bottomleft")
    screen.add_sprite(flora_03, (568, 1010), "bottomleft")
    screen.add_sprite(flora_03, (1598, 1010), "bottomleft")
    screen.add_sprite(flora_04, (1704, 1010), "bottomleft")

    screen.add_sprite(bg_02, (0, 1200), "bottomleft")

    (x, y) = screen.screen.get_rect().center
    (player, player_i) = screen.add_sprite(ufo_green, (x, y))
    screen.camera.player_index = player_i
    speed = 10
    setattr(screen, 'max_y', (layer1.rect.bottom - 60) - player.image.get_height() * 0.5)
    setattr(screen, 'min_y', (layer1.rect.top) + player.image.get_height() * 0.5)
    setattr(screen, 'max_x', (layer1.rect.right) - player.image.get_width() * 0.5)
    setattr(screen, 'min_x', (layer1.rect.left) + player.image.get_width() * 0.5)
    screen.camera.map_rect = layer1.rect

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
        
        if player.rect.left < self.min_x:
            player.rect.left = self.min_x
        if player.rect.top < self.min_y:
            player.rect.top = self.min_y
        if player.rect.right > self.max_x:
            player.rect.right = self.max_x
        if player.rect.bottom > self.max_y:
            player.rect.bottom = self.max_y
        
        player.rect.center += self.direction * speed
        self.camera.player = player.rect

        layer2_a.rect.x -= cloud_speed
        if layer2_a.rect.x < -layer1.rect.width:
            layer2_a.rect.x = layer1.rect.centerx * 2 - cloud_speed
        layer2_b.rect.x -= cloud_speed
        if layer2_b.rect.x < -layer1.rect.width:
            layer2_b.rect.x = layer1.rect.centerx * 2 - cloud_speed
    
    return controls