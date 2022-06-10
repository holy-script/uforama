import os
from random import randint
from classes.base import BaseScreen
import pygame as pg
from pygame.locals import *
from operator import sub
import math
import config as cf

crosshair_icon = os.path.join(os.path.dirname(__file__), '..', 'assets', 'crosshair_icon.png')
ufo_green = os.path.join(os.path.dirname(__file__), '..', 'assets', 'ufo_green.png')
ufo_blue = os.path.join(os.path.dirname(__file__), '..', 'assets', 'ufo_blue.png')
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
station_bad = os.path.join(os.path.dirname(__file__), '..', 'assets', 'station_bad.png')
station_good = os.path.join(os.path.dirname(__file__), '..', 'assets', 'station_good.png')
shield_bad = os.path.join(os.path.dirname(__file__), '..', 'assets', 'shield_bad.png')
shield_good = os.path.join(os.path.dirname(__file__), '..', 'assets', 'shield_good.png')
gun_01 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'gun_01.png')
bullet_01 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'bullet_01.png')

def play(camera, lvl):
    play = BaseScreen('Play', 'black', 1)
    play.set_camera(camera)
    play.create(True)
    play.camera.mouse.image = pg.image.load(crosshair_icon)
    play.to_copy = True
    play.triggers['LOSER'] = -1

    levels = {
        '1': level1
    }

    setattr(play, 'level', lvl)
    controls = levels[str(lvl)](play)
    play.pressed = pg.key.get_pressed()

    def effects(self):
        self.pressed = pg.key.get_pressed()
        controls(self)
    setattr(BaseScreen, 'update', effects)
    return play

def level1(screen):
    layer1 = screen.add_sprite('background', bg_00, (0, 0), "topleft")

    layer2_a = screen.add_sprite('background', bg_01, (0, layer1.rect.centery), "center")
    layer2_b = screen.add_sprite('background', bg_01, (layer1.rect.centerx * 2, layer1.rect.centery), "center")
    cloud_speed = 1

    screen.add_sprite('background', bg_03, (0, 1200), "bottomleft")

    screen.add_sprite('background', tree_04, (-6, 1010), "bottomleft")
    screen.add_sprite('background', tree_07, (118, 1010), "bottomleft")
    screen.add_sprite('background', tree_07, (234, 1010), "bottomleft")
    screen.add_sprite('background', tree_07, (550, 1010), "bottomleft")
    screen.add_sprite('background', tree_07, (688, 1010), "bottomleft")
    screen.add_sprite('background', tree_07, (790, 1010), "bottomleft")
    screen.add_sprite('background', tree_07, (1300, 1010), "bottomleft")
    screen.add_sprite('background', tree_07, (1424, 1010), "bottomleft")
    screen.add_sprite('background', tree_07, (1784, 1010), "bottomleft")
    screen.add_sprite('background', tree_09, (394, 1010), "bottomleft")
    screen.add_sprite('background', tree_02, (991, 1010), "bottomleft")
    screen.add_sprite('background', tree_06, (1560, 1010), "bottomleft")

    screen.add_sprite('background', flora_02, (1171, 1010), "bottomleft")
    screen.add_sprite('background', flora_01, (35, 1010), "bottomleft")
    screen.add_sprite('background', flora_01, (995, 1010), "bottomleft")
    screen.add_sprite('background', flora_03, (568, 1010), "bottomleft")
    screen.add_sprite('background', flora_03, (1598, 1010), "bottomleft")
    screen.add_sprite('background', flora_04, (1704, 1010), "bottomleft")

    enemy_shield = screen.add_sprite('background', shield_good, (layer1.rect.centerx, 357), "center")
    enemy_base = screen.add_sprite('background', station_good, (layer1.rect.centerx, 357), "center")
    #268 end game

    enemy_patrol = screen.add_sprite('enemies', ufo_blue, (layer1.rect.centerx, 357), "center", range_x=(enemy_base.rect.centerx - 250, enemy_base.rect.centerx + 250), range_y=(enemy_base.rect.centery - 100, enemy_base.rect.centery + 100), speed=(10, 5))

    screen.add_sprite('background', bg_02, (0, 1200), "bottomleft")

    (x, y) = screen.screen.get_rect().center

    setattr(screen, 'bullet_01_img', pg.image.load(bullet_01))

    setattr(screen, 'shooting', False)

    player = screen.add_sprite('player', ufo_green, (x, y))
    setattr(screen, 'max_y', (layer1.rect.bottom - 60) - player.image.get_height() * 0.5)
    setattr(screen, 'min_y', (layer1.rect.top) + player.image.get_height() * 0.5)
    setattr(screen, 'max_x', (layer1.rect.right) - player.image.get_width() * 0.5)
    setattr(screen, 'min_x', (layer1.rect.left) + player.image.get_width() * 0.5)
    screen.camera.map_rect = layer1.rect

    player_gun = screen.add_sprite('guns', gun_01, (0, 41), parent=player)

    setattr(screen, 'direction', pg.math.Vector2())

    def controls(self):

        layer2_a.rect.x -= cloud_speed
        if layer2_a.rect.x < -layer1.rect.width:
            layer2_a.rect.x = layer1.rect.centerx * 2 - cloud_speed
        layer2_b.rect.x -= cloud_speed
        if layer2_b.rect.x < -layer1.rect.width:
            layer2_b.rect.x = layer1.rect.centerx * 2 - cloud_speed

        if enemy_base.rect.top < 1010 - 268:
            enemy_shield.rect.centery += 1
            enemy_base.rect.centery += 1
        else:
            pg.event.post(pg.event.Event(self.triggers['LOSER']))
        
        # enemy_patrol.rect.centery = enemy_base.rect.top + 268 - enemy_patrol.rect.height / 2
        #330 for good

        if pg.mouse.get_pressed()[0]:
            if not self.shooting:
                self.add_sprite('bullets', bullet_01, (player_gun.rect.center), "center")
                self.shooting = True
        else:
            self.shooting = False
    
    return controls