import pygame as pg
from pygame.locals import *
import config as cf
import screens.splash as splash
import screens.home as home
import screens.game as game

class Director:
    def __init__(self, clock, cam):
        self.window = pg.display.get_surface()
        self.clock = clock
        self.cam = cam
        self.events = {}
        self.evt_count = 0
        self.in_transition = False
        self.entering = False
        self.counter = 0
        self.threshold = 0
        self.screens = {
            "logos": splash.logos,
            "banner": splash.banner,
            "menu": home.menu,
            "credits": home.credits,
            "options": home.options,
            "start": home.lvls,
            "play": game.play,
            "win": splash.win,
            "lose": splash.lose,
            "tutorial": home.tutorial,
            "objectives": home.objectives,
        }
        self.current = None

    def make_event(self, name):
        if name not in self.events:
            self.evt_count += 1
            self.events[name] = USEREVENT + self.evt_count
            return self.events[name]
    
    @staticmethod
    def translate(value, leftMin, leftMax, rightMin, rightMax):
        # Figure out how 'wide' each range is
        leftSpan = leftMax - leftMin
        rightSpan = rightMax - rightMin

        # Convert the left range into a 0-1 range (float)
        valueScaled = float(value - leftMin) / float(leftSpan)

        # Convert the 0-1 range into a value in the right range.
        return round(rightMin + (valueScaled * rightSpan))
    
    def start_screen(self, name, data=None):
        self.cam.clear_camera()
        if data:
            self.current = self.screens[name](self.cam, data)
        else:
            self.current = self.screens[name](self.cam)
        self.cam.set_texts(self.current.texts)
        self.threshold = self.current.count * cf.get_fps()
        self.in_transition = True
        self.entering = True
    
    def end_screen(self):
        self.in_transition = True
        self.entering = False

    def startup(self):
        pg.time.set_timer(self.make_event('FADE_OUT_LOGOS'), 2000, 1)
        pg.time.set_timer(self.make_event('FADE_IN_BANNER'), 3000, 1)
        pg.time.set_timer(self.make_event('FADE_OUT_BANNER'), 7000, 1)
        pg.time.set_timer(self.make_event('FADE_IN_MENU'), 8000, 1)

        pg.event.post(pg.event.Event(self.make_event('FADE_IN_LOGOS')))
    
    def transition(self):
        if self.entering:
            if self.counter < self.threshold:
                self.counter += 1
            elif self.counter >= self.threshold:
                self.counter = self.threshold
                self.in_transition = False
        else:
            if self.counter > 0:
                self.counter -= 1
            elif self.counter <= 0:
                self.counter = 0
                self.in_transition = False
        
        self.current.opacity(self.translate(self.counter, 0, self.threshold, 0, 255))

    def direct(self):
        if self.in_transition:
            self.transition()
        else:
            if self.current.dynamic:
                if not self.current.evts_added:
                    (self.events, self.evt_count) = self.current.evt_call(self.events, self.evt_count)
                    self.current.evts_added = True
                self.current.update()

        self.window.blit(self.current.screen, (0, 0))