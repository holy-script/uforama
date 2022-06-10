from plistlib import load
import pygame as pg
from pygame.locals import *
import math
import os
import config as cf

class GameSprite(pg.sprite.Sprite):
    def __init__(self, src, screen, point, pos, keepcopy=False):
        super().__init__()
        self.image = pg.image.load(src).convert_alpha()
        self.rect = self.image.get_rect()
        self.add(screen.camera)
        setattr(self.rect, pos, point)
        if keepcopy:
            self.img_copy = self.image.copy()
    
    def destroy(self):
        self.kill()
        #remove from arrays

class BulletSprite(pg.sprite.Sprite):
    def __init__(self, src, screen, point, pos):
        super().__init__()
        self.screen = screen
        self.image = pg.image.load(src).convert_alpha()
        self.rect = self.image.get_rect()
        self.add(screen.camera)
        setattr(self.rect, pos, point)
        self.img_copy = self.image.copy()
        self.old_rect = self.rect
        self.image = pg.transform.rotozoom(self.img_copy, self.screen.angle, 1).convert_alpha()
        self.rect = self.image.get_rect(center=self.old_rect.center)
        self.speed = 10
        self.pos = pg.math.Vector2(point)
        self.direction = pg.math.Vector2((math.cos(math.radians(self.screen.angle)) * self.speed, -math.sin(math.radians(self.screen.angle)) * self.speed))
        self.damage = 10

    def hit(self, sprite):
        sprite.health -= self.damage

    def update(self):
        self.pos += self.direction
        self.rect.center = self.pos
        if not self.screen.camera.map_rect.collidepoint(self.rect.center):
            self.kill()
        
        enemy_hit = pg.sprite.spritecollide(self, self.screen.enemy_group, False)
        if enemy_hit:
            [self.hit(enemy) for enemy in enemy_hit]
            self.kill()

class PlayerSprite(pg.sprite.Sprite):
    def __init__(self, src, screen, point, pos):
        super().__init__()
        self.screen = screen
        self.image = pg.image.load(src).convert_alpha()
        self.rect = self.image.get_rect()
        self.add(screen.camera)
        setattr(self.rect, pos, point)
        self.image = pg.image.load(src).convert_alpha()
        self.speed = 10
        self.health = 100
    
    def update(self):
        if self.screen.pressed[K_w]:
            self.screen.direction.y = -1
        elif self.screen.pressed[K_s]:
            self.screen.direction.y = 1
        else:
            self.screen.direction.y = 0
        
        if self.screen.pressed[K_d]:
            self.screen.direction.x = 1
        elif self.screen.pressed[K_a]:
            self.screen.direction.x = -1
        else:
            self.screen.direction.x = 0
        
        if self.rect.left < self.screen.min_x:
            self.rect.left = self.screen.min_x
        if self.rect.top < self.screen.min_y:
            self.rect.top = self.screen.min_y
        if self.rect.right > self.screen.max_x:
            self.rect.right = self.screen.max_x
        if self.rect.bottom > self.screen.max_y:
            self.rect.bottom = self.screen.max_y
        
        self.rect.center += self.screen.direction * self.speed
        self.screen.camera.player = self.rect

class GunSprite(pg.sprite.Sprite):
    def __init__(self, src, screen, offset, parent, damage=10):
        super().__init__()
        self.screen = screen
        self.image = pg.image.load(src).convert_alpha()
        self.rect = self.image.get_rect()
        self.add(screen.camera)
        self.img_copy = self.image.copy()
        self.parent = parent
        self.offset = offset
        self.rect.center = self.parent.rect.center + pg.math.Vector2(self.offset)
        self.damage = damage
        
    def update(self):
        self.rect.center = self.parent.rect.center + pg.math.Vector2(self.offset)

        dx = pg.mouse.get_pos()[0] + self.screen.camera.offset.x - self.rect.centerx
        dy = pg.mouse.get_pos()[1] + self.screen.camera.offset.y - self.rect.centery + 41
        rad = math.atan2(-dy, dx)
        rad %= 2*math.pi
        angle = math.degrees(rad)
        self.screen.angle = angle

        self.old_rect = self.rect
        self.image = pg.transform.rotozoom(self.img_copy, angle, 1).convert_alpha()
        self.rect = self.image.get_rect(center=self.old_rect.center)

class EnemySprite(pg.sprite.Sprite):
    def __init__(self, src, screen, point, pos, range_x, range_y, speed):
        super().__init__()
        self.screen = screen
        self.image = pg.image.load(src).convert_alpha()
        self.rect = self.image.get_rect()
        self.add(screen.camera)
        setattr(self.rect, pos, point)
        self.image = pg.image.load(src).convert_alpha()
        self.speed = 10
        self.health = 100
        self.range_x = range_x
        self.range_y = range_y
        self.speed = pg.math.Vector2(speed)
        self.add(self.screen.enemy_group)
    
    def update(self):
        if self.rect.centerx > self.range_x[1] or self.rect.centerx < self.range_x[0]:
            self.rect.centerx -= self.speed.x
            self.speed.x *= -1
        else:
            self.rect.centerx += self.speed.x
        
        if self.rect.centery > self.range_y[1] or self.rect.centery < self.range_y[0]:
            self.rect.centery -= self.speed.y
            self.speed.y *= -1
        else:
            self.rect.centery += self.speed.y
        
        if self.health <= 0:
            PoofSprite(self.screen, self.rect.center)
            self.kill()

class PoofSprite(pg.sprite.Sprite):
    def __init__(self, screen, point):
        super().__init__()
        self.src = [
            os.path.join(os.path.dirname(__file__), '..', 'assets', 'poof_0.png'),
            os.path.join(os.path.dirname(__file__), '..', 'assets', 'poof_1.png'),
            os.path.join(os.path.dirname(__file__), '..', 'assets', 'poof_2.png'),
            os.path.join(os.path.dirname(__file__), '..', 'assets', 'poof_3.png'),
            os.path.join(os.path.dirname(__file__), '..', 'assets', 'poof_4.png'),
            os.path.join(os.path.dirname(__file__), '..', 'assets', 'poof_5.png'),
            os.path.join(os.path.dirname(__file__), '..', 'assets', 'poof_6.png'),
            os.path.join(os.path.dirname(__file__), '..', 'assets', 'poof_7.png'),
            os.path.join(os.path.dirname(__file__), '..', 'assets', 'poof_8.png'),
        ]
        self.src.reverse()
        self.frames = []
        [self.frames.append(pg.image.load(frame).convert_alpha()) for frame in self.src]
        self.frame_duration = 0.75 * cf.get_fps() / len(self.frames)
        self.frame_counter = 1
        self.counter = 0
        self.screen = screen
        self.point = point
        self.image = self.frames[0]
        self.rect = self.frames[0].get_rect(center=self.point)
        self.add(self.screen.camera)
    
    def update(self):
        self.image = self.frames[0]
        self.rect = self.frames[0].get_rect(center=self.point)
        self.counter += 1

        if self.frame_counter >= len(self.frames):
            self.kill()

        if self.counter >= self.frame_duration:
            self.frames.append(self.frames.pop(0))
            self.counter = 0
            self.frame_counter += 1

class BoomSprite(pg.sprite.Sprite):
    def __init__(self, screen, point):
        super().__init__()
        self.src = [
            os.path.join(os.path.dirname(__file__), '..', 'assets', 'boom_00.png'),
            os.path.join(os.path.dirname(__file__), '..', 'assets', 'boom_01.png'),
            os.path.join(os.path.dirname(__file__), '..', 'assets', 'boom_02.png'),
            os.path.join(os.path.dirname(__file__), '..', 'assets', 'boom_03.png'),
            os.path.join(os.path.dirname(__file__), '..', 'assets', 'boom_04.png'),
            os.path.join(os.path.dirname(__file__), '..', 'assets', 'boom_05.png'),
            os.path.join(os.path.dirname(__file__), '..', 'assets', 'boom_06.png'),
            os.path.join(os.path.dirname(__file__), '..', 'assets', 'boom_07.png'),
            os.path.join(os.path.dirname(__file__), '..', 'assets', 'boom_08.png'),
            os.path.join(os.path.dirname(__file__), '..', 'assets', 'boom_09.png'),
            os.path.join(os.path.dirname(__file__), '..', 'assets', 'boom_10.png'),
            os.path.join(os.path.dirname(__file__), '..', 'assets', 'boom_11.png'),
        ]
        self.src.reverse()
        self.frames = []
        [self.frames.append(pg.image.load(frame).convert_alpha()) for frame in self.src]
        self.frame_duration = 1 * cf.get_fps() / len(self.frames)
        self.frame_counter = 1
        self.counter = 0
        self.screen = screen
        self.point = point
        self.image = self.frames[0]
        self.rect = self.frames[0].get_rect(center=self.point)
        self.add(self.screen.camera)
    
    def update(self):
        self.image = self.frames[0]
        self.rect = self.frames[0].get_rect(center=self.point)
        self.counter += 1

        if self.frame_counter >= len(self.frames):
            self.kill()

        if self.counter >= self.frame_duration:
            self.frames.append(self.frames.pop(0))
            self.counter = 0
            self.frame_counter += 1

class MineSprite(pg.sprite.Sprite):
    def __init__(self, src, screen, point, pos):
        super().__init__()
        self.screen = screen
        self.image = pg.image.load(src).convert_alpha()
        self.rect = self.image.get_rect()
        self.add(screen.camera)
        setattr(self.rect, pos, point)
        self.img_copy = self.image.copy()
        self.angle = 0
        self.damage = 20

    def hit(self, sprite):
        sprite.health -= self.damage

    def update(self):
        self.angle += 1
        if self.angle >= 360:
            self.angle = 0

        self.old_rect = self.rect
        self.image = pg.transform.rotozoom(self.img_copy, self.angle, 1).convert_alpha()
        self.rect = self.image.get_rect(center=self.old_rect.center)
        
        # enemy_hit = pg.sprite.spritecollide(self, self.screen.enemy_group, False)
        # if enemy_hit:
        #     [self.hit(enemy) for enemy in enemy_hit]
        #     self.kill()
