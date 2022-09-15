import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
# from pygame.locals import *
from pygame.locals import (
RLEACCEL,
)

class PressSpace(pygame.sprite.Sprite):
    def __init__(self,SCREEN_WIDTH,SCREEN_HEIGHT,PATH):
        super(PressSpace, self).__init__()
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.PATH = PATH
        self.surf = pygame.image.load("Resources/press_space.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()

        # Put the center of surf at the center of the display
        self.surf_center = (
            (self.SCREEN_WIDTH - self.surf.get_width()) / 2,
            (self.SCREEN_HEIGHT - self.surf.get_height()) / 2
        )


class Fish(pygame.sprite.Sprite):
    def __init__(self,SCREEN_WIDTH,SCREEN_HEIGHT,PATH):
        super(Fish, self).__init__()
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.PATH = PATH
        self.surf = pygame.image.load("Resources/bigfish.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()

        # Put the center of surf at the center of the display
        self.location = (
            (self.SCREEN_WIDTH - self.surf.get_width()) / 2,
            (self.SCREEN_HEIGHT - self.surf.get_height()) / 3.5
        )


class FishAdventure(pygame.sprite.Sprite):
    def __init__(self,SCREEN_WIDTH,SCREEN_HEIGHT,PATH):
        super(FishAdventure, self).__init__()
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.PATH = PATH
        self.surf = pygame.image.load("Resources/fish_adventure.png").convert_alpha()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()

        # Put the center of surf at the center of the display
        self.location = (
            (self.SCREEN_WIDTH - self.surf.get_width()) / 2,
            (self.SCREEN_HEIGHT - self.surf.get_height()) / 5.5
        )

