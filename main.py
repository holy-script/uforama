import pygame
from pygame.locals import *
import sys

def main():
    pygame.init()
    window = pygame.display.set_mode((1000, 750))
    pygame.display.set_caption('Hello, World!')
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        window.fill((0, 0, 0))
        pygame.display.update()

if __name__ == '__main__':
    main()
