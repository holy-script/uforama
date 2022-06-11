import pygame as pg
from pygame.locals import *
import math
import os
import config as cf

class GameSprite(pg.sprite.Sprite):
    def __init__(self, src, screen, point, pos, sticky):
        super().__init__()
        self.image = pg.image.load(src).convert_alpha()
        self.rect = self.image.get_rect()
        self.add(screen.camera)
        setattr(self.rect, pos, screen.camera.offset + point)
        self.pos = pos
        self.point = point
        self.sticky = sticky
        self.screen = screen
        self.cropped = False
        self.crop_area = pg.rect.Rect(0, 0, 0, 0)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
    
    def update(self):
        if self.sticky:
            setattr(self.rect, self.pos, self.screen.camera.offset + self.point)

    def destroy(self):
        self.kill()

class BulletSprite(pg.sprite.Sprite):
    def __init__(self, src, screen, point, pos, parent, dmg=10):
        super().__init__()
        self.screen = screen
        self.image = pg.image.load(src).convert_alpha()
        self.rect = self.image.get_rect()
        self.add(screen.camera)
        setattr(self.rect, pos, point)
        self.img_copy = self.image.copy()
        self.old_rect = self.rect
        self.parent = parent
        self.image = pg.transform.rotozoom(self.img_copy, self.parent.angle, 1).convert_alpha()
        self.rect = self.image.get_rect(center=self.old_rect.center)
        self.speed = 10
        self.pos = pg.math.Vector2(point)
        self.direction = pg.math.Vector2(
            (math.cos(math.radians(self.parent.angle)) * self.speed, -math.sin(math.radians(self.parent.angle)) * self.speed)
        )
        self.damage = dmg

    def hit(self, sprite):
        sprite.health -= self.damage

    def update(self):
        self.pos += self.direction
        self.rect.center = self.pos
        if not self.screen.camera.map_rect.collidepoint(self.rect.center):
            self.kill()
        
        if self.parent == self.screen.camera.player:
            enemy_hit = pg.sprite.spritecollide(self, self.screen.enemy_group, False)
            if enemy_hit:
                [self.hit(enemy) for enemy in enemy_hit]
                if self.damage == 50:
                    BoomSprite(self.screen, self.rect.center)
                self.kill()
        else:
            player_hit = pg.sprite.spritecollide(self, self.screen.player_group, False)
            if player_hit:
                [self.hit(player) for player in player_hit]
                self.kill()

class MineSprite(pg.sprite.Sprite):
    def __init__(self, src, screen, point, pos, parent, dmg=10):
        super().__init__()
        self.screen = screen
        self.image = pg.image.load(src).convert_alpha()
        self.rect = self.image.get_rect()
        self.add(screen.camera)
        setattr(self.rect, pos, point)
        self.img_copy = self.image.copy()
        self.parent = parent
        self.angle = self.parent.angle
        self.damage = dmg

    def hit(self, sprite):
        sprite.health -= self.damage

    def update(self):
        self.angle += 1
        if self.angle >= 360:
            self.angle = 0

        self.old_rect = self.rect
        self.image = pg.transform.rotozoom(self.img_copy, self.angle, 1).convert_alpha()
        self.rect = self.image.get_rect(center=self.old_rect.center)

        player_hit = pg.sprite.spritecollide(self, self.screen.player_group, False)
        if player_hit:
            [self.hit(player) for player in player_hit]
            BoomSprite(self.screen, self.rect.center)
            self.kill()      

class PlayerSprite(pg.sprite.Sprite):
    def __init__(self, screen, point):
        super().__init__()
        self.screen = screen
        self.image = pg.image.load(
            os.path.join(os.path.dirname(__file__), '..', 'assets', 'ufo_green.png')
        ).convert_alpha()
        self.rect = self.image.get_rect()
        self.add(screen.camera)
        setattr(self.rect, "center", point)
        self.speed = 10
        self.health = 100
        self.gun = GunSprite(
            os.path.join(os.path.dirname(__file__), '..', 'assets', 'gun_green.png'),
            self.screen,
            (0, 41),
            self
        )
        self.bullet = os.path.join(os.path.dirname(__file__), '..', 'assets', 'bullet_green.png')
        self.rocket = os.path.join(os.path.dirname(__file__), '..', 'assets', 'rocket.png')
        self.shooting = False
        self.add(self.screen.player_group)
        self.angle = 0
        self.radius = self.gun.image.get_size()[0] / 2
        self.zoom = 1
        self.use_rocket = False

    def toggle_rocket(self, use):
        self.use_rocket = use

    def update(self):
        self.zoom = cf.get_player_gun_z()

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

        if pg.mouse.get_pressed()[0]:
            if not self.shooting:
                circ = pg.math.Vector2(
                    self.radius * math.cos(math.radians(self.angle)),
                    -self.radius * math.sin(math.radians(self.angle))
                )
                if not self.use_rocket:
                    BulletSprite(self.bullet, self.screen, self.gun.rect.center + circ, "center", self, 25)
                else:
                    BulletSprite(self.rocket, self.screen, self.gun.rect.center + circ, "center", self, 50)
                self.shooting = True
        else:
            self.shooting = False
        
        if self.health <= 0:
            print("dead!")

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

        if self.parent == self.screen.camera.player:
            dx = pg.mouse.get_pos()[0] + self.screen.camera.offset.x - self.rect.centerx
            dy = pg.mouse.get_pos()[1] + self.screen.camera.offset.y - self.rect.centery
        else:
            dx = self.screen.camera.player.center[0] - self.rect.centerx
            dy = self.screen.camera.player.center[1] - self.rect.centery

        rad = math.atan2(-dy, dx)
        rad %= 2*math.pi
        angle = math.degrees(rad)
        self.parent.angle = angle

        self.old_rect = self.rect
        self.image = pg.transform.rotozoom(self.img_copy, angle, self.parent.zoom).convert_alpha()
        self.rect = self.image.get_rect(center=self.old_rect.center)

enemies = {
    'yellow': {
        'image': os.path.join(os.path.dirname(__file__), '..', 'assets', 'ufo_yellow.png'),
        'gun': os.path.join(os.path.dirname(__file__), '..', 'assets', 'gun_yellow.png'),
        'offsets': [
            (0, 34)
        ],
        'shoot': os.path.join(os.path.dirname(__file__), '..', 'assets', 'bullet_yellow.png'),
        'create': BulletSprite,
    },
    'beige': {
        'image': os.path.join(os.path.dirname(__file__), '..', 'assets', 'ufo_beige.png'),
        'gun': os.path.join(os.path.dirname(__file__), '..', 'assets', 'gun_beige.png'),
        'offsets': [
            (-25, 43),
            (25, 43)
        ],
        'shoot': os.path.join(os.path.dirname(__file__), '..', 'assets', 'bullet_beige.png'),
        'create': BulletSprite,
    },
    'pink': {
        'image': os.path.join(os.path.dirname(__file__), '..', 'assets', 'ufo_pink.png'),
        'gun': os.path.join(os.path.dirname(__file__), '..', 'assets', 'gun_pink.png'),
        'offsets': [
            (0, 50)
        ],
        'shoot': os.path.join(os.path.dirname(__file__), '..', 'assets', 'mine.png'),
        'create': MineSprite,
    },
    'blue': {
        'image': os.path.join(os.path.dirname(__file__), '..', 'assets', 'ufo_blue.png'),
        'gun': None,
        'offsets': [],
        'shoot': None,
        'create': None,
    },
}

powerups = {
    'shield': {
        'src': os.path.join(os.path.dirname(__file__), '..', 'assets', 'power_shield.png'),
        'effect': lambda screen: pg.event.post(pg.event.Event(screen.triggers['SHIELD'])),
    },
    'rocket': {
        'src': os.path.join(os.path.dirname(__file__), '..', 'assets', 'power_rocket.png'),
        'effect': lambda screen: pg.event.post(pg.event.Event(screen.triggers['ROCKET'])),
    },
    'slow': {
        'src': os.path.join(os.path.dirname(__file__), '..', 'assets', 'power_slow.png'),
        'effect': lambda screen: pg.event.post(pg.event.Event(screen.triggers['SLOW'])),
    },
}

class EnemySprite(pg.sprite.Sprite):
    def __init__(self, screen, point, type, range_x, range_y, speed):
        super().__init__()
        self.screen = screen
        self.image = pg.image.load(enemies[type]['image']).convert_alpha()
        self.rect = self.image.get_rect()
        self.add(screen.camera)
        setattr(self.rect, "center", point)
        self.health = 100
        self.range_x = range_x
        self.range_y = range_y
        self.speed = pg.math.Vector2(speed)
        self.add(self.screen.enemy_group)
        self.guns = [
            GunSprite(enemies[type]['gun'], self.screen, offset, self) 
            for offset in enemies[type]['offsets'] 
            if offset
        ]
        self.type = type
        self.shooting = False
        self.angle = 0
        if self.guns:
            self.radius = self.guns[0].image.get_size()[0] / 2
        self.zoom = 1
    
    def shoot(self, gun):
        circ = pg.math.Vector2(
            self.radius * math.cos(math.radians(self.angle)),
            -self.radius * math.sin(math.radians(self.angle))
        )
        enemies[self.type]['create'](enemies[self.type]['shoot'], self.screen, gun.rect.center + circ, "center", self, cf.get_dmg(self.type))
    
    def set_speed(self, speed):
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
        
        if self.health <= 0:
            PowerupSprite(self.screen, self.rect.center, 'shield')
            PoofSprite(self.screen, self.rect.center)
            [gun.kill() for gun in self.guns]
            self.kill()
        
        if pg.mouse.get_pressed()[-1]:
            if not self.shooting:
                [self.shoot(gun) for gun in self.guns]
                self.shooting = True
        else:
            self.shooting = False

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
    def __init__(self, screen, point, big=False):
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

class PowerupSprite(pg.sprite.Sprite):
    def __init__(self, screen, point, type):
        super().__init__()
        self.screen = screen
        self.image = pg.image.load(powerups[type]['src']).convert_alpha()
        self.rect = self.image.get_rect()
        self.add(screen.camera)
        setattr(self.rect, "center", point)
        self.timeout = 20
        self.counter = 0
        self.flash_time = 1 * cf.get_fps()
        self.type = type
    
    @staticmethod
    def translate(value, leftMin, leftMax, rightMin, rightMax):
        # Figure out how 'wide' each range is
        leftSpan = leftMax - leftMin
        rightSpan = rightMax - rightMin

        # Convert the left range into a 0-1 range (float)
        valueScaled = float(value - leftMin) / float(leftSpan)

        # Convert the 0-1 range into a value in the right range.
        return round(rightMin + (valueScaled * rightSpan))
    
    def update(self):
        self.counter += 1
        self.image.set_alpha(self.translate(self.counter, 0, self.flash_time, 126, 255))
        if self.counter >= self.flash_time:
            self.counter = 0
            self.timeout -= 1
        
        if self.timeout <= 0:
            self.kill()
        
        player_take = pg.sprite.spritecollide(self, self.screen.player_group, False)
        if player_take:
            powerups[self.type]['effect'](self.screen)
            self.kill()