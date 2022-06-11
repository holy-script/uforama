import pygame as pg
from pygame.locals import *
import os
import config as cf


class BasicCamera(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display = pg.display.get_surface()
        self.texts = []
        self.mouse = pg.sprite.Sprite()
        self.mouse.image = pg.image.load(os.path.join(os.path.dirname(__file__), "..", 'assets', 'mouse_icon.png'))
        self.mouse.image = pg.transform.rotate(self.mouse.image, 30)
        self.mouse.rect = self.mouse.image.get_rect()
        pg.mouse.set_visible(False)
        self.offset = pg.math.Vector2()
        (self.half_width, self.half_height) = self.display.get_size()
        self.half_width /= 2
        self.half_height /= 2
        self.player = pg.Rect(0, 0, 0, 0)
        self.cam_box = {
            "left": cf.config['width'] / 8,
            "top": cf.config['height'] / 8,
        }
        self.cam_rect = pg.Rect(
            self.cam_box['left'], self.cam_box['top'], 
            self.display.get_rect().width - (2 * self.cam_box['left']), self.display.get_rect().height - (2 * self.cam_box['top'])
        )
        self.follow_player = False
        self.map_rect = pg.Rect(0, 0, 0, 0)

    def set_texts(self, texts):
        self.texts = texts
    
    def clear_texts(self):
        self.texts = []
    
    def clear_camera(self):
        self.clear_texts()
        self.empty()
    
    def player_camera(self):
        if self.player.left < self.cam_rect.left and self.player.left > (self.map_rect.left + self.cam_box['left']):
            self.cam_rect.left = self.player.left
        if self.player.right > self.cam_rect.right and self.player.right < (self.map_rect.right - self.cam_box['left']):
            self.cam_rect.right = self.player.right
        if self.player.top < self.cam_rect.top and self.player.top > (self.map_rect.top + self.cam_box['top']):
            self.cam_rect.top = self.player.top
        if self.player.bottom > self.cam_rect.bottom and self.player.bottom < (self.map_rect.bottom - self.cam_box['top']):
            self.cam_rect.bottom = self.player.bottom

        self.offset.x = self.cam_rect.left - self.cam_box['left']
        self.offset.y = self.cam_rect.top - self.cam_box['top']

    def mouse_maker(self):
        self.mouse.rect.center =  pg.mouse.get_pos() + pg.math.Vector2(10, 20)
        self.display.blit(self.mouse.image, self.mouse.rect)

    def offset_draw(self, sprite):
        offset_pos = sprite.rect.topleft - self.offset
        if hasattr(sprite, 'cropped'):
            if sprite.cropped:
                self.display.blit(sprite.image, sprite.point, sprite.crop_area)
            else:
                self.display.blit(sprite.image, offset_pos)
        else:
            self.display.blit(sprite.image, offset_pos)

    def render(self):
        [self.offset_draw(sprite) for sprite in self.sprites()]
            
        if self.follow_player:
            self.player_camera()
            
        [self.display.blit(text[0], text[0].get_rect(center=text[1])) for text in self.texts]

        self.mouse_maker()