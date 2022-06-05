import pygame as pg
from pygame.locals import *
import os


class BasicCamera(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display = pg.display.get_surface()
        self.texts = []
        self.mouse = pg.sprite.Sprite()
        self.mouse.image = pg.image.load(os.path.join(os.path.dirname(__file__), 'assets', 'mouse_icon.png'))
        self.mouse.image = pg.transform.rotate(self.mouse.image, 30)
        self.mouse.rect = self.mouse.image.get_rect()
        pg.mouse.set_visible(False)
        self.offset = pg.math.Vector2()
        (self.half_width, self.half_height) = self.display.get_size()
        self.half_width /= 2
        self.half_height /= 2
        (self.player_x, self.player_y) = self.display.get_rect().center

    def set_texts(self, texts):
        self.texts = texts
    
    def clear_texts(self):
        self.texts = []
    
    def clear_camera(self):
        self.clear_texts()
        self.empty()

    def render(self):
        for (index, sprite) in enumerate(self.sprites()):
            self.offset.x = self.player_x - self.half_width
            self.offset.y = self.player_y - self.half_height
            offset_pos = sprite.rect.topleft - self.offset
            self.display.blit(sprite.image, offset_pos)
            
        for text in self.texts:
            self.display.blit(text[0], text[0].get_rect(center=text[1]))

        self.mouse.rect.center =  pg.mouse.get_pos() + pg.math.Vector2(10, 20)
        self.display.blit(self.mouse.image, self.mouse.rect)