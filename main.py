import pygame as pg
from pygame.locals import *
import sys
import config as cf
from classes.camera import BasicCamera
from classes.director import Director
from pygame import mixer as mx
import os

def main():
    pg.init()
    mx.init()
    mx.music.load(os.path.join(os.path.dirname(__file__), 'assets', 'main_track.wav'))
    mx.music.set_volume(0.3 if not cf.get_mute() else 0)
    mx.music.play(-1)
    mx.set_num_channels(10)
    pg.display.set_caption('uforama!')
    window = pg.display.set_mode(cf.get_size())
    fps = cf.get_fps()
    debug = True
    font = pg.font.SysFont(None, 36)
    clock = pg.time.Clock()
    cam = BasicCamera()
    director = Director(clock, cam)
    director.startup()

    def terminate():
        mx.music.stop()
        mx.music.unload()
        pg.quit()
        sys.exit()
    
    def restart():
        mx.music.stop()
        mx.music.unload()
        pg.quit()
        main()

    def show_fps():
        txt = font.render(str(round(clock.get_fps())), True, pg.Color('limegreen'), pg.Color('magenta3'))
        window.blit(txt, txt.get_rect())

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
                        if director.current.name != 'Play':
                            if pg.mouse.get_pressed()[0]:
                                click = mx.Sound(os.path.join(os.path.dirname(__file__), 'assets', 'sfx_click.wav'))
                                click.set_volume(0.2 if not cf.get_mute() else 0)
                                mx.Channel(9).play(click)
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
                            if director.current.name == 'Play':
                                cam.follow_player = True
                                if director.current.evts_added:
                                    if event.type == director.events['LOSER']:
                                        lose = mx.Sound(os.path.join(os.path.dirname(__file__), 'assets', 'sfx_lose.wav'))
                                        lose.set_volume(0.2 if not cf.get_mute() else 0)
                                        mx.Channel(6).play(lose)
                                        director.end_screen()
                                        pg.time.set_timer(director.events['FADE_IN_LOSE'], 1000, 1)
                                    if event.type == director.events['WINNER']:
                                        win = mx.Sound(os.path.join(os.path.dirname(__file__), 'assets', 'sfx_win.wav'))
                                        win.set_volume(0.2 if not cf.get_mute() else 0)
                                        mx.Channel(7).play(win)
                                        director.end_screen()
                                        pg.time.set_timer(director.events['FADE_IN_WIN'], 1000, 1)
                                    if event.type == director.events['ROCKET']:
                                        cf.set_player_gun_z(1.5)
                                        [player.toggle_rocket(True) for player in director.current.player_group]
                                        pg.time.set_timer(director.events['ROCKET_END'], 5000, 1)
                                    if event.type == director.events['ROCKET_END']:
                                        cf.set_player_gun_z(1)
                                        [player.toggle_rocket(False) for player in director.current.player_group]
                                    if event.type == director.events['SHIELD']:
                                        cf.set_dmg_enemies(0, 0, 0)
                                        pg.time.set_timer(director.events['SHIELD_END'], 5000, 1)
                                    if event.type == director.events['SHIELD_END']:
                                        cf.set_dmg_enemies(10, 4, 12)
                                    if event.type == director.events['SLOW']:
                                        cf.set_speed_enemies((2, 1), (1.2, 1.2), (0.8, 1.6))
                                        [enemy.set_speed(cf.get_speed(enemy.type)) for enemy in director.current.enemy_group]
                                        pg.time.set_timer(director.events['SLOW_END'], 5000, 1)
                                    if event.type == director.events['SLOW_END']:
                                        cf.set_speed_enemies((10, 5), (6, 6), (4, 8))
                                        [enemy.set_speed(cf.get_speed(enemy.type)) for enemy in director.current.enemy_group]
                                    if event.type == director.events['FADE_IN_LOSE']:
                                        director.start_screen('lose')
                                        pg.time.set_timer(director.events['FADE_OUT_LOSE'], 2000, 1)
                                    if event.type == director.events['FADE_IN_WIN']:
                                        director.start_screen('win')
                                        pg.time.set_timer(director.events['FADE_OUT_WIN'], 2000, 1)
                            else:
                                if event.type == director.events['MENU_CLICK']:
                                    director.end_screen()
                                    pg.time.set_timer(director.events['FADE_IN_MENU'], 1000, 1)
                                if director.current.name == 'Options':
                                    if event.type == director.events['MUTE SOUNDS_CLICK']:
                                        cf.set_mute(not cf.get_mute())
                                        if cf.get_mute():
                                            mx.music.pause()
                                        else:
                                            mx.music.play()
                                    if event.type == director.events['RESIZE HD/SD_CLICK']:
                                        if cf.config['width'] == 720:
                                            cf.set_size(960, 720)
                                        else:
                                            cf.set_size(720, 576)
                                        restart()
                                    if event.type == director.events['EASY/HARD_CLICK']:
                                        if cf.config['firerate']['yellow'] == 3:
                                            cf.set_firerate(2, 1, 3)
                                        else:
                                            cf.set_firerate(3, 2, 5)
                                if director.current.name == 'Levels':
                                    if event.type == director.events['HOW TO PLAY?_CLICK']:
                                        director.end_screen()
                                        pg.time.set_timer(director.events['FADE_IN_HOW TO PLAY?'], 1000, 1)
                                    if event.type == director.events['FADE_IN_HOW TO PLAY?']:
                                        director.start_screen('tutorial')
                                    if event.type == director.events['OBJECTIVES_CLICK']:
                                        director.end_screen()
                                        pg.time.set_timer(director.events['FADE_IN_OBJECTIVES'], 1000, 1)
                                    if event.type == director.events['FADE_IN_OBJECTIVES']:
                                        director.start_screen('objectives')
                                    if event.type == director.events['1.1_CLICK']:
                                        director.end_screen()
                                        pg.time.set_timer(director.events['FADE_IN_1.1'], 1000, 1)
                                        cam.set_crosshair()
                                        mx.music.stop()
                                        mx.music.unload()
                                        mx.music.load(os.path.join(os.path.dirname(__file__), 'assets', 'fight_track.wav'))
                                        mx.music.set_volume(0.3 if not cf.get_mute() else 0)
                                        mx.music.play(-1)
                                    if event.type == director.events['FADE_IN_1.1']:
                                        director.start_screen('play', '1.1')
                                    if event.type == director.events['1.2_CLICK']:
                                        director.end_screen()
                                        pg.time.set_timer(director.events['FADE_IN_1.2'], 1000, 1)
                                        cam.set_crosshair()
                                        mx.music.stop()
                                        mx.music.unload()
                                        mx.music.load(os.path.join(os.path.dirname(__file__), 'assets', 'fight_track.wav'))
                                        mx.music.set_volume(0.3 if not cf.get_mute() else 0)
                                        mx.music.play(-1)
                                    if event.type == director.events['FADE_IN_1.2']:
                                        director.start_screen('play', '1.2')
                                    if event.type == director.events['1.3_CLICK']:
                                        director.end_screen()
                                        pg.time.set_timer(director.events['FADE_IN_1.3'], 1000, 1)
                                        cam.set_crosshair()
                                        mx.music.stop()
                                        mx.music.unload()
                                        mx.music.load(os.path.join(os.path.dirname(__file__), 'assets', 'fight_track.wav'))
                                        mx.music.set_volume(0.3 if not cf.get_mute() else 0)
                                        mx.music.play(-1)
                                    if event.type == director.events['FADE_IN_1.3']:
                                        director.start_screen('play', '1.3')
                                    if event.type == director.events['2.1_CLICK']:
                                        director.end_screen()
                                        pg.time.set_timer(director.events['FADE_IN_2.1'], 1000, 1)
                                        cam.set_crosshair()
                                        mx.music.stop()
                                        mx.music.unload()
                                        mx.music.load(os.path.join(os.path.dirname(__file__), 'assets', 'fight_track.wav'))
                                        mx.music.set_volume(0.3 if not cf.get_mute() else 0)
                                        mx.music.play(-1)
                                    if event.type == director.events['FADE_IN_2.1']:
                                        director.start_screen('play', '2.1')
                                    if event.type == director.events['2.2_CLICK']:
                                        director.end_screen()
                                        pg.time.set_timer(director.events['FADE_IN_2.2'], 1000, 1)
                                        cam.set_crosshair()
                                        mx.music.stop()
                                        mx.music.unload()
                                        mx.music.load(os.path.join(os.path.dirname(__file__), 'assets', 'fight_track.wav'))
                                        mx.music.set_volume(0.3 if not cf.get_mute() else 0)
                                        mx.music.play(-1)
                                    if event.type == director.events['FADE_IN_2.2']:
                                        director.start_screen('play', '2.2')
                                    if event.type == director.events['2.3_CLICK']:
                                        director.end_screen()
                                        pg.time.set_timer(director.events['FADE_IN_2.3'], 1000, 1)
                                        cam.set_crosshair()
                                        mx.music.stop()
                                        mx.music.unload()
                                        mx.music.load(os.path.join(os.path.dirname(__file__), 'assets', 'fight_track.wav'))
                                        mx.music.set_volume(0.3 if not cf.get_mute() else 0)
                                        mx.music.play(-1)
                                    if event.type == director.events['FADE_IN_2.3']:
                                        director.start_screen('play', '2.3')
                                    if event.type == director.events['3.1_CLICK']:
                                        director.end_screen()
                                        pg.time.set_timer(director.events['FADE_IN_3.1'], 1000, 1)
                                        cam.set_crosshair()
                                        mx.music.stop()
                                        mx.music.unload()
                                        mx.music.load(os.path.join(os.path.dirname(__file__), 'assets', 'fight_track.wav'))
                                        mx.music.set_volume(0.3 if not cf.get_mute() else 0)
                                        mx.music.play(-1)
                                    if event.type == director.events['FADE_IN_3.1']:
                                        director.start_screen('play', '3.1')
                                    if event.type == director.events['3.2_CLICK']:
                                        director.end_screen()
                                        pg.time.set_timer(director.events['FADE_IN_3.2'], 1000, 1)
                                        cam.set_crosshair()
                                        mx.music.stop()
                                        mx.music.unload()
                                        mx.music.load(os.path.join(os.path.dirname(__file__), 'assets', 'fight_track.wav'))
                                        mx.music.set_volume(0.3 if not cf.get_mute() else 0)
                                        mx.music.play(-1)
                                    if event.type == director.events['FADE_IN_3.2']:
                                        director.start_screen('play', '3.2')
                                    if event.type == director.events['3.3_CLICK']:
                                        director.end_screen()
                                        pg.time.set_timer(director.events['FADE_IN_3.3'], 1000, 1)
                                        cam.set_crosshair()
                                        mx.music.stop()
                                        mx.music.unload()
                                        mx.music.load(os.path.join(os.path.dirname(__file__), 'assets', 'fight_track.wav'))
                                        mx.music.set_volume(0.3 if not cf.get_mute() else 0)
                                        mx.music.play(-1)
                                    if event.type == director.events['FADE_IN_3.3']:
                                        director.start_screen('play', '3.3')
                else:
                    if director.current.name == 'Win' or director.current.name == 'Lose':
                        mx.music.stop()
                        mx.music.unload()
                        mx.music.load(os.path.join(os.path.dirname(__file__), 'assets', 'main_track.wav'))
                        mx.music.set_volume(0.3 if not cf.get_mute() else 0)
                        mx.music.play(-1)
                        if event.type == director.events['FADE_OUT_LOSE']:
                            cam.set_pointer()
                            director.end_screen()
                            pg.time.set_timer(director.events['FADE_IN_MENU'], 1500, 1)
                        if event.type == director.events['FADE_OUT_WIN']:
                            cam.set_pointer()
                            director.end_screen()
                            pg.time.set_timer(director.events['FADE_IN_MENU'], 1500, 1)
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
