import os
from random import randint
from classes.base import BaseScreen
import pygame as pg
from pygame.locals import *
from operator import sub
import config as cf
from classes.sprite import PlayerSprite, EnemySprite

bg_00 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'bg_00.png')
bg_01 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'bg_01.png')
bg_02 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'bg_02.png')
bg_03 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'bg_03.png')
bg_10 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'bg_10.png')
bg_11 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'bg_11.png')
bg_12 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'bg_12.png')
bg_13 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'bg_13.png')
bg_14 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'bg_14.png')
bg_20 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'bg_20.png')
bg_21 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'bg_21.png')
bg_22 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'bg_22.png')
bg_23 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'bg_23.png')
bg_24 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'bg_24.png')
bg_25 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'bg_25.png')
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
health_bar = os.path.join(os.path.dirname(__file__), '..', 'assets', 'health_bar.png')
health_val = os.path.join(os.path.dirname(__file__), '..', 'assets', 'health_val.png')
tracker = os.path.join(os.path.dirname(__file__), '..', 'assets', 'tracker.png')
flag = os.path.join(os.path.dirname(__file__), '..', 'assets', 'flag.png')
point = os.path.join(os.path.dirname(__file__), '..', 'assets', 'point.png')
cloud1 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'cloud1.png')
cloud2 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'cloud2.png')
cloud3 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'cloud3.png')
cloud4 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'cloud4.png')
cloud5 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'cloud5.png')
cloud6 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'cloud6.png')
cloud7 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'cloud7.png')
cloud8 = os.path.join(os.path.dirname(__file__), '..', 'assets', 'cloud8.png')

def play(camera, lvl):
    play = BaseScreen('Play', 'black', 1)
    play.set_camera(camera)
    play.create(True)
    play.triggers['LOSER'] = -1
    play.triggers['WINNER'] = -1
    play.triggers['ROCKET'] = -1
    play.triggers['SHIELD'] = -1
    play.triggers['SLOW'] = -1
    play.triggers['ROCKET_END'] = -1
    play.triggers['SHIELD_END'] = -1
    play.triggers['SLOW_END'] = -1
    play.triggers['FADE_IN_LOSE'] = -1
    play.triggers['FADE_IN_WIN'] = -1
    play.triggers['FADE_OUT_LOSE'] = -1
    play.triggers['FADE_OUT_WIN'] = -1

    levels = {
        '1': level1,
        '2': level2,
        '3': level3,
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
    layer1 = screen.add_sprite(bg_00, (0, 0), "topleft")

    layer2_a = screen.add_sprite(bg_01, (0, layer1.rect.centery), "center")
    layer2_b = screen.add_sprite(bg_01, (layer1.rect.centerx * 2, layer1.rect.centery), "center")
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

    enemy_shield = screen.add_sprite(shield_bad, (layer1.rect.centerx, 357), "center")
    enemy_base = screen.add_sprite(station_bad, (layer1.rect.centerx, 357), "center")

    player_shield = screen.add_sprite(shield_good, (layer1.rect.centerx, 0), "midbottom")
    player_base = screen.add_sprite(station_good, (layer1.rect.centerx, 0), "midbottom")

    EnemySprite(
        screen, 
        (layer1.rect.centerx, 357), 
        'yellow', 
        (enemy_base.rect.centerx - 700, enemy_base.rect.centerx + 700), 
        (enemy_base.rect.centery - 100, enemy_base.rect.centery + 100), 
    )

    screen.add_sprite(bg_02, (0, 1200), "bottomleft")

    (x, y) = screen.screen.get_rect().center

    player = PlayerSprite(screen, (x, y))
    setattr(screen, 'max_y', (layer1.rect.bottom - 60) - player.image.get_height() * 0.5)
    setattr(screen, 'min_y', (layer1.rect.top) + player.image.get_height() * 0.5)
    setattr(screen, 'max_x', (layer1.rect.right) - player.image.get_width() * 0.5)
    setattr(screen, 'min_x', (layer1.rect.left) + player.image.get_width() * 0.5)
    screen.camera.map_rect = layer1.rect

    setattr(screen, 'direction', pg.math.Vector2())

    hv = screen.add_sprite(health_val, pg.math.Vector2(29, 32), "topleft", True)
    hv.cropped = True
    screen.add_sprite(health_bar, pg.math.Vector2(20, 20), "topleft", True)
    track = screen.add_sprite(tracker, pg.math.Vector2(screen.camera.half_width, screen.camera.half_height * 2 - 20), "center", True)

    wave_points = [
        {
            'x_off': 0,
            'alive': True,
            'sprite': None,
            'triggered': False,
            'enemies': [
                {
                    'type': 'blue',
                    'spawn': (layer1.rect.centerx, enemy_base.rect.centery + 50),
                    'x_range': (enemy_base.rect.centerx - 250, enemy_base.rect.centerx + 250),
                    'y_range': (enemy_base.rect.centery - 90, enemy_base.rect.centery + 90),
                },
            ]
        },
        {
            'x_off': 0,
            'alive': True,
            'sprite': None,
            'triggered': False,
            'enemies': [
                {
                    'type': 'beige',
                    'spawn': (layer1.rect.centerx, enemy_base.rect.centery + 50),
                    'x_range': (enemy_base.rect.centerx - 250, enemy_base.rect.centerx + 250),
                    'y_range': (enemy_base.rect.centery - 90, enemy_base.rect.centery + 90),
                },
            ]
        },
        {
            'x_off': 0,
            'alive': True,
            'sprite': None,
            'triggered': False,
            'enemies': [
                {
                    'type': 'pink',
                    'spawn': (layer1.rect.centerx, enemy_base.rect.centery + 50),
                    'x_range': (enemy_base.rect.centerx - 250, enemy_base.rect.centerx + 250),
                    'y_range': (enemy_base.rect.centery - 90, enemy_base.rect.centery + 90),
                },
            ]
        },
    ]

    setattr(screen, 'wave_points', wave_points)
    setattr(screen, 'base_down', False)

    def create_wave(i):
        wave_points[i-1]['sprite'] = screen.add_sprite(point, pg.math.Vector2(screen.camera.half_width - track.width / 2 + track.width * i / (len(wave_points) + 1), screen.camera.half_height * 2 - 20), "center", True)
        wave_points[i-1]['x_off'] = screen.camera.half_width - track.width / 2 + track.width * i / (len(wave_points) + 1)

    [create_wave(i) for i in range(1, len(wave_points) + 1)]

    flag_mark = screen.add_sprite(flag, pg.math.Vector2(screen.camera.half_width - track.width / 2, screen.camera.half_height * 2 - 20), "center", True)

    base_speed = 1

    def controls(self):
        if self.wave_points:
            if not self.wave_points[0]['triggered']:
                if self.wave_points[0]['sprite'].rect.centerx == flag_mark.rect.centerx:
                    self.wave_points[0]['triggered'] = True
            if not self.enemy_group.sprites():
                self.wave_points[0]['alive'] = False
                if not self.wave_points[0]['alive']:
                    flag_mark.point = (self.wave_points[0]['x_off'], flag_mark.point[1])
                    [
                        EnemySprite(self, enemy['spawn'], enemy['type'], enemy['x_range'], enemy['y_range']) 
                        for enemy in self.wave_points[0]['enemies']
                    ]
                    self.wave_points.pop(0)
        else:
            if not self.enemy_group.sprites():
                flag_mark.point = pg.math.Vector2(screen.camera.half_width + track.width / 2, screen.camera.half_height * 2 - 20)
                if self.base_down:
                    pg.event.post(pg.event.Event(self.triggers['WINNER']))
        

        hv.crop_area = hv.image.get_rect(width=screen.translate(player.health, 0, 100, 0, hv.width))

        layer2_a.rect.x -= cloud_speed
        if layer2_a.rect.x < -layer1.rect.width:
            layer2_a.rect.x = layer1.rect.centerx * 2 - cloud_speed
        layer2_b.rect.x -= cloud_speed
        if layer2_b.rect.x < -layer1.rect.width:
            layer2_b.rect.x = layer1.rect.centerx * 2 - cloud_speed

        if enemy_base.rect.top < 1010 - 268:
            if flag_mark.rect.centerx == screen.camera.offset.x + screen.camera.half_width - track.width / 2:
                if pg.sprite.spritecollide(enemy_shield, self.enemy_group, False):
                    enemy_shield.rect.centery += base_speed
                    enemy_base.rect.centery += base_speed
            else:
                if enemy_base.rect.bottom > 0:
                    enemy_shield.rect.centery -= base_speed
                    enemy_base.rect.centery -= base_speed
                else:
                    if player_base.rect.bottom < layer1.rect.top + 149:
                        player_shield.rect.centery += base_speed
                        player_base.rect.centery += base_speed
                    else:
                        if player_base.rect.top < 1010 - 330:
                            if pg.sprite.spritecollide(player_shield, self.player_group, False):
                                player_shield.rect.centery += base_speed
                                player_base.rect.centery += base_speed
                        else:
                            self.base_down = True
        else:
            pg.event.post(pg.event.Event(self.triggers['LOSER']))
    
    return controls

def level2(screen):
    layer1 = screen.add_sprite(bg_10, (0, 0), "topleft")
    screen.add_sprite(bg_11, (0, 0), "topleft")
    c1 = screen.add_sprite(cloud5, (1235, 630), "center")
    screen.add_sprite(bg_13, (0, 1240), "bottomleft")
    c2 = screen.add_sprite(cloud6, (550, 196), "center")
    screen.add_sprite(bg_14, (0, 1080), "bottomleft")
    c3 = screen.add_sprite(cloud7, (1465, 258), "center")
    c4 = screen.add_sprite(cloud8, (693, 384), "center")

    enemy_shield = screen.add_sprite(shield_bad, (layer1.rect.centerx, 357), "center")
    enemy_base = screen.add_sprite(station_bad, (layer1.rect.centerx, 357), "center")
    player_shield = screen.add_sprite(shield_good, (layer1.rect.centerx, 0), "midbottom")
    player_base = screen.add_sprite(station_good, (layer1.rect.centerx, 0), "midbottom")

    screen.add_sprite(bg_12, (0, 1240), "bottomleft")

    (x, y) = screen.screen.get_rect().center

    player = PlayerSprite(screen, (x, y))
    setattr(screen, 'max_y', (layer1.rect.bottom - 100) - player.image.get_height() * 0.5)
    setattr(screen, 'min_y', (layer1.rect.top) + player.image.get_height() * 0.5)
    setattr(screen, 'max_x', (layer1.rect.right) - player.image.get_width() * 0.5)
    setattr(screen, 'min_x', (layer1.rect.left) + player.image.get_width() * 0.5)
    screen.camera.map_rect = layer1.rect

    setattr(screen, 'direction', pg.math.Vector2())

    hv = screen.add_sprite(health_val, pg.math.Vector2(29, 32), "topleft", True)
    hv.cropped = True
    screen.add_sprite(health_bar, pg.math.Vector2(20, 20), "topleft", True)
    track = screen.add_sprite(tracker, pg.math.Vector2(screen.camera.half_width, screen.camera.half_height * 2 - 20), "center", True)

    EnemySprite(
        screen, 
        (layer1.rect.centerx, 357), 
        'yellow', 
        (enemy_base.rect.centerx - 700, enemy_base.rect.centerx + 700), 
        (enemy_base.rect.centery - 100, enemy_base.rect.centery + 100), 
    )

    wave_points = [
        {
            'x_off': 0,
            'alive': True,
            'sprite': None,
            'triggered': False,
            'enemies': [
                {
                    'type': 'blue',
                    'spawn': (layer1.rect.centerx, enemy_base.rect.centery + 50),
                    'x_range': (enemy_base.rect.centerx - 250, enemy_base.rect.centerx + 250),
                    'y_range': (enemy_base.rect.centery - 90, enemy_base.rect.centery + 90),
                },
            ]
        },
        {
            'x_off': 0,
            'alive': True,
            'sprite': None,
            'triggered': False,
            'enemies': [
                {
                    'type': 'beige',
                    'spawn': (layer1.rect.centerx, enemy_base.rect.centery + 50),
                    'x_range': (enemy_base.rect.centerx - 250, enemy_base.rect.centerx + 250),
                    'y_range': (enemy_base.rect.centery - 90, enemy_base.rect.centery + 90),
                },
            ]
        },
        {
            'x_off': 0,
            'alive': True,
            'sprite': None,
            'triggered': False,
            'enemies': [
                {
                    'type': 'pink',
                    'spawn': (layer1.rect.centerx, enemy_base.rect.centery + 50),
                    'x_range': (enemy_base.rect.centerx - 250, enemy_base.rect.centerx + 250),
                    'y_range': (enemy_base.rect.centery - 90, enemy_base.rect.centery + 90),
                },
            ]
        },
    ]

    setattr(screen, 'wave_points', wave_points)
    setattr(screen, 'base_down', False)

    def create_wave(i):
        wave_points[i-1]['sprite'] = screen.add_sprite(point, pg.math.Vector2(screen.camera.half_width - track.width / 2 + track.width * i / (len(wave_points) + 1), screen.camera.half_height * 2 - 20), "center", True)
        wave_points[i-1]['x_off'] = screen.camera.half_width - track.width / 2 + track.width * i / (len(wave_points) + 1)

    [create_wave(i) for i in range(1, len(wave_points) + 1)]

    flag_mark = screen.add_sprite(flag, pg.math.Vector2(screen.camera.half_width - track.width / 2, screen.camera.half_height * 2 - 20), "center", True)

    base_speed = 1
    
    def controls(self):
        c3.rect.centerx += 2
        if c3.rect.left > layer1.rect.right:
            c3.rect.right = layer1.rect.left
        c4.rect.centerx += 2
        if c4.rect.left > layer1.rect.right:
            c4.rect.right = layer1.rect.left

        c1.rect.centerx += 1
        if c1.rect.left > layer1.rect.right:
            c1.rect.right = layer1.rect.left
        c2.rect.centerx += 1
        if c2.rect.left > layer1.rect.right:
            c2.rect.right = layer1.rect.left        

        if self.wave_points:
            if not self.wave_points[0]['triggered']:
                if self.wave_points[0]['sprite'].rect.centerx == flag_mark.rect.centerx:
                    self.wave_points[0]['triggered'] = True
            if not self.enemy_group.sprites():
                self.wave_points[0]['alive'] = False
                if not self.wave_points[0]['alive']:
                    flag_mark.point = (self.wave_points[0]['x_off'], flag_mark.point[1])
                    [
                        EnemySprite(self, enemy['spawn'], enemy['type'], enemy['x_range'], enemy['y_range']) 
                        for enemy in self.wave_points[0]['enemies']
                    ]
                    self.wave_points.pop(0)
        else:
            if not self.enemy_group.sprites():
                flag_mark.point = pg.math.Vector2(screen.camera.half_width + track.width / 2, screen.camera.half_height * 2 - 20)
                if self.base_down:
                    pg.event.post(pg.event.Event(self.triggers['WINNER']))

        hv.crop_area = hv.image.get_rect(width=screen.translate(player.health, 0, 100, 0, hv.width))

        if enemy_base.rect.top < 930 - 268:
            if flag_mark.rect.centerx == screen.camera.offset.x + screen.camera.half_width - track.width / 2:
                if pg.sprite.spritecollide(enemy_shield, self.enemy_group, False):
                    enemy_shield.rect.centery += base_speed
                    enemy_base.rect.centery += base_speed
            else:
                if enemy_base.rect.bottom > 0:
                    enemy_shield.rect.centery -= base_speed
                    enemy_base.rect.centery -= base_speed
                else:
                    if player_base.rect.bottom < layer1.rect.top + 149:
                        player_shield.rect.centery += base_speed
                        player_base.rect.centery += base_speed
                    else:
                        if player_base.rect.top < 930 - 330:
                            if pg.sprite.spritecollide(player_shield, self.player_group, False):
                                player_shield.rect.centery += base_speed
                                player_base.rect.centery += base_speed
                        else:
                            self.base_down = True
        else:
            pg.event.post(pg.event.Event(self.triggers['LOSER']))

    return controls

def level3(screen):
    layer1 = screen.add_sprite(bg_20, (0, 0), "topleft")
    screen.add_sprite(bg_21, (0, 0), "topleft")
    c1 = screen.add_sprite(cloud1, (1465, 258), "center")
    screen.add_sprite(bg_22, (0, 1240), "bottomleft")
    c2 = screen.add_sprite(cloud2, (550, 384), "center")
    screen.add_sprite(bg_23, (0, 1240), "bottomleft")
    c3 = screen.add_sprite(cloud3, (1235, 630), "center")
    c4 = screen.add_sprite(cloud4, (693, 196), "center")

    enemy_shield = screen.add_sprite(shield_bad, (layer1.rect.centerx, 357), "center")
    enemy_base = screen.add_sprite(station_bad, (layer1.rect.centerx, 357), "center")
    player_shield = screen.add_sprite(shield_good, (layer1.rect.centerx, 0), "midbottom")
    player_base = screen.add_sprite(station_good, (layer1.rect.centerx, 0), "midbottom")

    screen.add_sprite(bg_24, (0, 1160), "bottomleft")
    screen.add_sprite(bg_25, (0, 0), "topleft")

    (x, y) = screen.screen.get_rect().center

    player = PlayerSprite(screen, (x, y))
    setattr(screen, 'max_y', (layer1.rect.bottom - 100) - player.image.get_height() * 0.5)
    setattr(screen, 'min_y', (layer1.rect.top) + player.image.get_height() * 0.5)
    setattr(screen, 'max_x', (layer1.rect.right) - player.image.get_width() * 0.5)
    setattr(screen, 'min_x', (layer1.rect.left) + player.image.get_width() * 0.5)
    screen.camera.map_rect = layer1.rect

    setattr(screen, 'direction', pg.math.Vector2())

    hv = screen.add_sprite(health_val, pg.math.Vector2(29, 32), "topleft", True)
    hv.cropped = True
    screen.add_sprite(health_bar, pg.math.Vector2(20, 20), "topleft", True)
    track = screen.add_sprite(tracker, pg.math.Vector2(screen.camera.half_width, screen.camera.half_height * 2 - 20), "center", True)

    EnemySprite(
        screen, 
        (layer1.rect.centerx, 357), 
        'yellow', 
        (enemy_base.rect.centerx - 700, enemy_base.rect.centerx + 700), 
        (enemy_base.rect.centery - 100, enemy_base.rect.centery + 100), 
    )

    wave_points = [
        {
            'x_off': 0,
            'alive': True,
            'sprite': None,
            'triggered': False,
            'enemies': [
                {
                    'type': 'blue',
                    'spawn': (layer1.rect.centerx, enemy_base.rect.centery + 50),
                    'x_range': (enemy_base.rect.centerx - 250, enemy_base.rect.centerx + 250),
                    'y_range': (enemy_base.rect.centery - 90, enemy_base.rect.centery + 90),
                },
            ]
        },
        {
            'x_off': 0,
            'alive': True,
            'sprite': None,
            'triggered': False,
            'enemies': [
                {
                    'type': 'beige',
                    'spawn': (layer1.rect.centerx, enemy_base.rect.centery + 50),
                    'x_range': (enemy_base.rect.centerx - 250, enemy_base.rect.centerx + 250),
                    'y_range': (enemy_base.rect.centery - 90, enemy_base.rect.centery + 90),
                },
            ]
        },
        {
            'x_off': 0,
            'alive': True,
            'sprite': None,
            'triggered': False,
            'enemies': [
                {
                    'type': 'pink',
                    'spawn': (layer1.rect.centerx, enemy_base.rect.centery + 50),
                    'x_range': (enemy_base.rect.centerx - 250, enemy_base.rect.centerx + 250),
                    'y_range': (enemy_base.rect.centery - 90, enemy_base.rect.centery + 90),
                },
            ]
        },
    ]

    setattr(screen, 'wave_points', wave_points)
    setattr(screen, 'base_down', False)

    def create_wave(i):
        wave_points[i-1]['sprite'] = screen.add_sprite(point, pg.math.Vector2(screen.camera.half_width - track.width / 2 + track.width * i / (len(wave_points) + 1), screen.camera.half_height * 2 - 20), "center", True)
        wave_points[i-1]['x_off'] = screen.camera.half_width - track.width / 2 + track.width * i / (len(wave_points) + 1)

    [create_wave(i) for i in range(1, len(wave_points) + 1)]

    flag_mark = screen.add_sprite(flag, pg.math.Vector2(screen.camera.half_width - track.width / 2, screen.camera.half_height * 2 - 20), "center", True)

    base_speed = 1
    
    def controls(self):
        c3.rect.centerx -= 2
        if c3.rect.right <= 0:
            c3.rect.left = layer1.rect.right
        c4.rect.centerx -= 2
        if c4.rect.right <= 0:
            c4.rect.left = layer1.rect.right

        c1.rect.centerx -= 1
        if c1.rect.right <= 0:
            c1.rect.left = layer1.rect.right
        c2.rect.centerx -= 1
        if c2.rect.right <= 0:
            c2.rect.left = layer1.rect.right

        if self.wave_points:
            if not self.wave_points[0]['triggered']:
                if self.wave_points[0]['sprite'].rect.centerx == flag_mark.rect.centerx:
                    self.wave_points[0]['triggered'] = True
            if not self.enemy_group.sprites():
                self.wave_points[0]['alive'] = False
                if not self.wave_points[0]['alive']:
                    flag_mark.point = (self.wave_points[0]['x_off'], flag_mark.point[1])
                    [
                        EnemySprite(self, enemy['spawn'], enemy['type'], enemy['x_range'], enemy['y_range']) 
                        for enemy in self.wave_points[0]['enemies']
                    ]
                    self.wave_points.pop(0)
        else:
            if not self.enemy_group.sprites():
                flag_mark.point = pg.math.Vector2(screen.camera.half_width + track.width / 2, screen.camera.half_height * 2 - 20)
                if self.base_down:
                    pg.event.post(pg.event.Event(self.triggers['WINNER']))

        hv.crop_area = hv.image.get_rect(width=screen.translate(player.health, 0, 100, 0, hv.width))

        if enemy_base.rect.top < 930 - 268:
            if flag_mark.rect.centerx == screen.camera.offset.x + screen.camera.half_width - track.width / 2:
                if pg.sprite.spritecollide(enemy_shield, self.enemy_group, False):
                    enemy_shield.rect.centery += base_speed
                    enemy_base.rect.centery += base_speed
            else:
                if enemy_base.rect.bottom > 0:
                    enemy_shield.rect.centery -= base_speed
                    enemy_base.rect.centery -= base_speed
                else:
                    if player_base.rect.bottom < layer1.rect.top + 149:
                        player_shield.rect.centery += base_speed
                        player_base.rect.centery += base_speed
                    else:
                        if player_base.rect.top < 930 - 330:
                            if pg.sprite.spritecollide(player_shield, self.player_group, False):
                                player_shield.rect.centery += base_speed
                                player_base.rect.centery += base_speed
                        else:
                            self.base_down = True
        else:
            pg.event.post(pg.event.Event(self.triggers['LOSER']))

    return controls