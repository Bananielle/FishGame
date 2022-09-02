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


class MainGame_background(pygame.sprite.Sprite):
    def __init__(self):
        super(MainGame_background, self).__init__()
        self.background_far = pygame.image.load(path + 'far.png')
        self.background_far = pygame.transform.scale(self.background_far,
                                                     (SCREEN_WIDTH, self.background_far.get_height() * 3))
        self.bgX_far = 0
        self.bgX2_far = self.background_far.get_width()

        self.background_middle = pygame.image.load(path + 'sand.png')
        self.background_middle = pygame.transform.scale(self.background_middle, (SCREEN_WIDTH, SCREEN_HEIGHT - 180))
        self.bgX_middle = 0
        self.bgX2_middle = self.background_middle.get_width()

        self.background_foreground = pygame.image.load(path + 'foreground-merged.png')
        self.background_foreground = pygame.transform.scale(self.background_foreground,
                                                            (SCREEN_WIDTH + 500, SCREEN_HEIGHT - 160))
        self.bgX_foreground = 0
        self.bgX2_foreground = self.background_foreground.get_width()

    def updateBackGrounds(self):
        self.bgX_far, self.bgX2_far = self.move_background(1.4, self.background_far.get_width(), self.bgX_far,
                                                           self.bgX2_far)
        self.bgX_middle, self.bgX2_middle = self.move_background(1.8, self.background_middle.get_width(),
                                                                 self.bgX_middle, self.bgX2_middle)
        self.bgX_foreground, self.bgX2_foreground = self.move_background(2, self.background_foreground.get_width(),
                                                                         self.bgX_foreground,
                                                                         self.bgX2_foreground)

    def move_background(self, speed, backgroundWidth, bgX, bgX2):
        # Make the background move
        bgX -= speed  # Move both background images back
        bgX2 -= speed

        if bgX < backgroundWidth * -1:  # If our bg is at the -width then reset its position
            bgX = backgroundWidth

        if bgX2 < backgroundWidth * -1:
            bgX2 = backgroundWidth

        return bgX, bgX2
