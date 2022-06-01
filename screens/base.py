import pygame as pg

class BaseScreen:
    def __init__(self, size, bg='white', transition_counter=3):
        self.size = size
        self.bg = bg
        self.counter = transition_counter
        self.sprites = []
    
    def create(self):
        self.screen = pg.Surface(self.size)
        self.screen.fill(pg.Color(self.bg))
    
    def add_sprite(self, path):
        self.sprites.append(pg.image.load(path))
    
    def get_sprites(self):
        return self.sprites