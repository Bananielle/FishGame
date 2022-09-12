import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
# from pygame.locals import *
from pygame.locals import (
    RLEACCEL,
)

path = "/Users/danielle/Documents/"
# Define constants for the screen width and height
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

class Picture():
    def __init__(self,path,filename):
        self.surf = pygame.image.load(path + filename).convert_alpha()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.surf_center = (
            (SCREEN_WIDTH - self.surf.get_width()) / 2,
            (SCREEN_HEIGHT - self.surf.get_height()) / 2
        )

    def setAtLocationFromCenter(self,x,y):
        self.location = (
            (SCREEN_WIDTH - self.surf.get_width()) / x,
            (SCREEN_HEIGHT - self.surf.get_height()) / y
        )

        gameover_image = pygame.image.load("gameover.png").convert_alpha()
        gameover_image.set_colorkey((0, 0, 0), RLEACCEL)
        gameover_image.location = (
            (SCREEN_WIDTH - gameover_image.get_width()) / 2,
            (SCREEN_HEIGHT - gameover_image.get_height()) / 1.3
        )

class GameOver(pygame.sprite.Sprite):
    def __init__(self,path,SCREEN_WIDTH,SCREEN_HEIGHT):
        super(GameOver, self).__init__()
        self.surf = pygame.image.load("gameover.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()

        # Put the center of surf at the center of the display
        self.surf_center = (
            (SCREEN_WIDTH - self.surf.get_width()) / 2,
            (SCREEN_HEIGHT - self.surf.get_height()) / 2.8
        )


class PressSpaceToReplay(pygame.sprite.Sprite):
    def __init__(self,path,SCREEN_WIDTH,SCREEN_HEIGHT):
        super(PressSpaceToReplay, self).__init__()
        self.surf = pygame.image.load("replay.png").convert_alpha()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()

        # Put the center of surf at the center of the display
        self.surf_center = (
            (SCREEN_WIDTH - self.surf.get_width()) / 2,
            (SCREEN_HEIGHT - self.surf.get_height()) / 1.5
        )

