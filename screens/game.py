import os
from random import randint
from screens.base import BaseScreen
import pygame as pg
from pygame.locals import *
from operator import sub
import math

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

    enemy_shield = screen.add_sprite(shield_good, (layer1.rect.centerx, 357), "center")[0]
    enemy_base = screen.add_sprite(station_good, (layer1.rect.centerx, 357), "center")[0]
    #268 end game

    enemy_patrol = screen.add_sprite(ufo_blue, (layer1.rect.centerx, 357), "center")[0]
    setattr(screen, 'patrol_min', enemy_base.rect.centerx - 250)
    setattr(screen, 'patrol_max', enemy_base.rect.centerx + 250)
    setattr(screen, 'patrol_speed', 10)

    screen.add_sprite(bg_02, (0, 1200), "bottomleft")

    (x, y) = screen.screen.get_rect().center

    player_gun = screen.add_sprite(gun_01, (x, y + 41), "center")[0]
    setattr(screen, 'gun_01_img', player_gun.image)

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

        player_gun.rect.center = (player.rect.centerx, player.rect.centery + 41)

        dx = pg.mouse.get_pos()[0] + self.camera.offset.x - player.rect.centerx
        dy = pg.mouse.get_pos()[1] + self.camera.offset.y - player.rect.centery + 41
        rad = math.atan2(-dy, dx)
        rad %= 2*math.pi
        angle = math.degrees(rad)
        old_rect = player_gun.rect
        player_gun.image = pg.transform.rotozoom(self.gun_01_img, angle, 1).convert_alpha()
        player_gun.rect = player_gun.image.get_rect(center=old_rect.center)

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
        
        if enemy_patrol.rect.centerx < self.patrol_max:
            enemy_patrol.rect.centerx += self.patrol_speed
        else:
            enemy_patrol.rect.centerx -= self.patrol_speed
            self.patrol_speed *= -1
        
        if enemy_patrol.rect.centerx < self.patrol_min:
            enemy_patrol.rect.centerx -= self.patrol_speed
            self.patrol_speed *= -1
        
        enemy_patrol.rect.centery = enemy_base.rect.top + 268 - enemy_patrol.rect.height / 2
        #330 for good
    
    return controls