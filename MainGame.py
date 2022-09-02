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


class MainGame(pygame.sprite.Sprite):
    def __init__(self):
        super(MainGame, self).__init__()