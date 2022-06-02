import pygame as pg
import config as cf

class BaseScreen:
    def __init__(self, bg='white', transition_count=3):
        self.size = cf.get_size()
        self.bg = bg
        self.count = transition_count
        self.sprites = []
        self.texts = []
    
    def create(self, dynamic=False):
        self.screen = pg.Surface(self.size)
        self.screen.fill(pg.Color(self.bg))
        self.dynamic = dynamic
    
    def opacity(self, val):
        self.screen.set_alpha(val)
        for sprite in self.sprites:
            sprite.image.set_alpha(val)
        for text in self.texts:
            text[0].set_alpha(val)
    
    def set_camera(self, camera):
        self.camera = camera
    
    def add_sprite(self, path, pos):
        sprite = pg.sprite.Sprite(self.camera)
        sprite.image = pg.image.load(path)
        sprite.rect = sprite.image.get_rect()
        sprite.rect.center = pos
        self.sprites.append(sprite)
        return sprite
    
    def add_text(self, size, pos, text, color, bg=None):
        font = pg.font.SysFont(None, size)
        txt = font.render(text, True, pg.Color(color), None if bg is None else pg.Color(bg))
        self.texts.append((txt, pos))