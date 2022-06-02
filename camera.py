import pygame as pg
from pygame.locals import *
import os
from operator import add


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

    def set_texts(self, texts):
        self.texts = texts
    
    def clear_texts(self):
        self.texts = []
    
    def clear_camera(self):
        self.clear_texts()
        self.empty()

    def render(self):
        for sprite in self.sprites():
            self.display.blit(sprite.image, sprite.rect)
            
        for text in self.texts:
            self.display.blit(text[0], text[0].get_rect(center=text[1]))

        self.mouse.rect.center =  tuple(map(add, pg.mouse.get_pos(), (10, 20)))
        self.display.blit(self.mouse.image, self.mouse.rect)