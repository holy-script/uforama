import pygame as pg
from pygame.locals import *
import math

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
    def __init__(self, src, screen, point, pos, angle):
        super().__init__()
        self.screen = screen
        self.image = pg.image.load(src).convert_alpha()
        self.rect = self.image.get_rect()
        self.add(screen.camera)
        setattr(self.rect, pos, point)
        self.img_copy = self.image.copy()
        self.old_rect = self.rect
        self.image = pg.transform.rotozoom(self.img_copy, angle, 1).convert_alpha()
        self.rect = self.image.get_rect(center=self.old_rect.center)
        self.speed = 10
        self.pos = pg.math.Vector2(point)
        self.direction = pg.math.Vector2((math.cos(math.radians(angle)) * self.speed, -math.sin(math.radians(angle)) * self.speed))

    def update(self):
        self.pos += self.direction
        self.rect.center = self.pos
        if not self.screen.camera.map_rect.collidepoint(self.rect.center):
            self.kill()

class PlayerSprite(pg.sprite.Sprite):
    def __init__(self, src, screen, point, pos,):
        super().__init__()
        self.screen = screen
        self.image = pg.image.load(src).convert_alpha()
        self.rect = self.image.get_rect()
        self.add(screen.camera)
        setattr(self.rect, pos, point)
        self.image = pg.image.load(src).convert_alpha()
        self.speed = 10
    
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
