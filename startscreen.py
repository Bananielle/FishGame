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

class StartScreen(pygame.sprite.Sprite):
    def __init__(self):
        super(StartScreen, self).__init__()
        self.surf = pygame.image.load(path + "press_space.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()

        # Put the center of surf at the center of the display
        self.surf_center = (
            (SCREEN_WIDTH - self.surf.get_width()) / 2,
            (SCREEN_HEIGHT - self.surf.get_height()) / 2
        )


class Fish(pygame.sprite.Sprite):
    def __init__(self):
        super(Fish, self).__init__()
        self.surf = pygame.image.load(path + "bigfish.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()

        # Put the center of surf at the center of the display
        self.location = (
            (SCREEN_WIDTH - self.surf.get_width()) / 2,
            (SCREEN_HEIGHT - self.surf.get_height()) / 3.5
        )


class FishAdventure(pygame.sprite.Sprite):
    def __init__(self):
        super(FishAdventure, self).__init__()
        self.surf = pygame.image.load(path + "fish_adventure.png").convert_alpha()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()

        # Put the center of surf at the center of the display
        self.location = (
            (SCREEN_WIDTH - self.surf.get_width()) / 2,
            (SCREEN_HEIGHT - self.surf.get_height()) / 5.5
        )

