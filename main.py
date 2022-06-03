import pygame as pg
from pygame.locals import *
import sys
import config as cf
from camera import BasicCamera
from director import Director

pg.init()
pg.display.set_caption('Hello, World!')
window = pg.display.set_mode(cf.get_size())
fps = cf.get_fps()
debug = True
font = pg.font.SysFont(None, 36)
clock = pg.time.Clock()
cam = BasicCamera()
director = Director(clock, cam)
director.startup()

def terminate():
    pg.quit()
    sys.exit()

def show_fps():
    txt = font.render(str(round(clock.get_fps())), True, pg.Color('limegreen'), pg.Color('magenta3'))
    window.blit(txt, txt.get_rect())

def main():
    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == director.events['FADE_IN_LOGOS']:
                director.start_screen('logos')
            if event.type == director.events['FADE_OUT_LOGOS']:
                director.end_screen()
            if event.type == director.events['FADE_IN_BANNER']:
                director.start_screen('banner')
            if event.type == director.events['FADE_OUT_BANNER']:
                director.end_screen()
            if event.type == director.events['FADE_IN_MENU']:
                director.start_screen('menu')
            if director.current:
                if director.current.dynamic:
                    if director.current.evts_added:
                        if event.type == director.events['PLAY!_CLICK']:
                            print("Play clicked")
                        if event.type == director.events['OPTIONS_CLICK']:
                            print("Options clicked")
                        if event.type == director.events['CREDITS_CLICK']:
                            print("Credits clicked")
                        if event.type == director.events['EXIT_CLICK']:
                            print("Exit clicked")
        
        window.fill(pg.Color('black'))
        director.direct()
        cam.render()

        if debug:
            show_fps()

        pg.display.update()
        clock.tick(fps)

if __name__ == '__main__':
    main()
