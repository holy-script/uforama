import pygame as pg
from pygame.locals import *

class BasicCamera(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display = pg.display.get_surface()
        self.texts = []

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