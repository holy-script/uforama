import pygame as pg
from pygame.locals import *
import sys
import config as cf

pg.init()
pg.display.set_caption('Hello, World!')
window = pg.display.set_mode(cf.get_size())
fps = cf.get_fps()
running = True
debug = True
font = pg.font.SysFont(None, 36)
clock = pg.time.Clock()

def terminate():
    pg.quit()
    sys.exit()

def show_fps():
    txt = font.render(str(round(clock.get_fps())), True, pg.Color('limegreen'), pg.Color('magenta3'))
    window.blit(txt, txt.get_rect())


def main():
    while running:
        for event in pg.event.get():
            if event.type == QUIT:
                terminate()
        
        window.fill(pg.Color('black'))

        if debug:
            show_fps()
            
        pg.display.update()
        clock.tick(fps)

if __name__ == '__main__':
    main()
