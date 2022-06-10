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

    def update(self):
        self.pos += self.direction
        self.rect.center = self.pos
        if not self.screen.camera.map_rect.collidepoint(self.rect.center):
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