import pygame as pg
import config as cf
from classes.sprite import GameSprite
from classes.sprite import BulletSprite
from classes.sprite import PlayerSprite
from classes.sprite import GunSprite
from classes.sprite import EnemySprite

class BaseScreen:
    def __init__(self, name, bg='white', transition_count=3):
        self.size = cf.get_size()
        self.bg = bg
        self.count = transition_count
        self.sprites = {}
        self.texts = []
        self.name = name
        self.btns = {}
        self.evts_added = False
        self.btn_states = {}
        self.triggers = {}
        self.types = {}
        self.pressed = {}
        self.angle = 0
    
    def create(self, dynamic=False):
        self.screen = pg.Surface(self.size)
        self.screen.fill(pg.Color(self.bg))
        self.dynamic = dynamic
    
    def opacity(self, val):
        self.screen.set_alpha(val)
        [
            [sprite.image.set_alpha(val) for sprite in self.sprites[layer]] for layer in self.sprites
        ]
        [text[0].set_alpha(val) for text in self.texts]
    
    def set_camera(self, camera):
        self.camera = camera
    
    def add_sprite(self, layer, path, point, pos='center', parent=None, range_x=(-100, 100), range_y=(-100, 100), speed=(10, 0)):
        if layer == 'bullets':
            sprite = BulletSprite(path, self, point, pos)
        elif layer == 'player':
            sprite = PlayerSprite(path, self, point, pos)
        elif layer == 'guns':
            sprite = GunSprite(path, self, point, parent)
        elif layer == 'enemies':
            sprite = EnemySprite(path, self, point, pos, range_x, range_y, speed)
        else:
            sprite = GameSprite(path, self, point, pos)
        if layer in self.sprites:
            self.sprites[layer].append(sprite)
        else:
            self.sprites[layer] = [sprite]
        return sprite
    
    def add_text(self, size, pos, text, color, bg=None):
        font = pg.font.SysFont(None, size)
        txt = font.render(text, True, pg.Color(color), None if bg is None else pg.Color(bg))
        self.texts.append((txt, pos))
        return (txt, pos, len(self.texts) - 1)

    def create_btn(self, name, font_size, color, x, y, def_path, btn_color):
        self.btns[name] = {
            f'{name}_x': x,
            f'{name}_y': y,
            f'{name}_y_active': y + 2,
            f'{name}_btn': self.add_sprite(def_path, self.screen.get_rect(center=(x, y)).center),
            f'{name}_txt': self.add_text(font_size, self.screen.get_rect(center=(x, y)).center, name, color),
            f'{name}_evt': f'{name.upper()}_CLICK',
            'evt_code': -1,
            'triggered': False,
            'btn_color': btn_color,
        }
    
    def change_btn(self, index, color, state):
        self.sprites[index].image = self.btn_states[color][state]
    
    def change_textpos(self, index, pos):
        self.texts[index] = (self.texts[index][0], pos)
    
    def evt_call(self, evts, evt_count):
        for name in self.btns:
            evt_count += 1
            evts[self.btns[name][f'{name}_evt']] = evt_count
            self.btns[name]['evt_code'] = evt_count
            evt_count += 1
            evts[f'FADE_IN_{name.upper()}'] = evt_count
        for name in self.triggers:
            evt_count += 1
            evts[name] = evt_count
            self.triggers[name] = evt_count
        return (evts, evt_count)
    
    def handle_btn_clicks(self):
        for name in self.btns:
            btn_data = self.btns[name]
            if btn_data[f'{name}_btn'][0].rect.collidepoint(pg.mouse.get_pos()):
                if pg.mouse.get_pressed()[0]:
                    self.change_btn(btn_data[f'{name}_btn'][1], btn_data['btn_color'], 'active')
                    btn_data[f'{name}_btn'][0].rect.centery = btn_data[f'{name}_y_active']
                    if not btn_data['triggered']:
                        pg.event.post(pg.event.Event(btn_data['evt_code']))
                        btn_data['triggered'] = True
                else:
                    self.change_btn(btn_data[f'{name}_btn'][1], btn_data['btn_color'], 'hover')
                    btn_data[f'{name}_btn'][0].rect.centery = btn_data[f'{name}_y']
                    if btn_data['triggered']:
                        btn_data['triggered'] = False
                self.change_textpos(btn_data[f'{name}_txt'][-1], btn_data[f'{name}_btn'][0].rect.center)
            else:
                self.change_btn(btn_data[f'{name}_btn'][1], btn_data['btn_color'], 'normal')