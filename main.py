import pygame as pg
from pygame.locals import *
import sys
import config as cf
from classes.camera import BasicCamera
from classes.director import Director

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
                director.start_screen('play', 1)
            if director.current:
                if director.current.dynamic:
                    if director.current.evts_added:
                        if director.current.name == 'Menu':
                            if event.type == director.events['START!_CLICK']:
                                director.end_screen()
                                pg.time.set_timer(director.events['FADE_IN_START!'], 1500, 1)
                            if event.type == director.events['OPTIONS_CLICK']:
                                director.end_screen()
                                pg.time.set_timer(director.events['FADE_IN_OPTIONS'], 1500, 1)
                            if event.type == director.events['CREDITS_CLICK']:
                                director.end_screen()
                                pg.time.set_timer(director.events['FADE_IN_CREDITS'], 1500, 1)
                            if event.type == director.events['EXIT_CLICK']:
                                director.end_screen()
                                pg.time.set_timer(QUIT, 1500, 1)
                            if event.type == director.events['FADE_IN_CREDITS']:
                                director.start_screen('credits')
                            if event.type == director.events['FADE_IN_OPTIONS']:
                                director.start_screen('options')
                            if event.type == director.events['FADE_IN_START!']:
                                director.start_screen('start')
                        else:
                            # if event.type == director.events['MENU_CLICK']:
                            #     director.end_screen()
                            #     pg.time.set_timer(director.events['FADE_IN_MENU'], 1000, 1)
                            if director.current.name == 'Levels':
                                if event.type == director.events['1_CLICK']:
                                    director.end_screen()
                                    pg.time.set_timer(director.events['FADE_IN_1'], 1000, 1)
                                if event.type == director.events['FADE_IN_1']:
                                    director.start_screen('play', 1)
                            if director.current.name == 'Play':
                                cam.follow_player = True
                                if event.type == director.events['LOSER']:
                                    #director.end_screen()
                                    #lose banner
                                    director
        
        window.fill(pg.Color('black'))
        director.direct()
        cam.render()
        cam.update()

        if debug:
            show_fps()

        pg.display.update()
        clock.tick(fps)

if __name__ == '__main__':
    main()
