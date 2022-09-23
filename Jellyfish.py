import pygame, random

# Import pygame.locals for easier access to key coordinates. Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    QUIT,
)

# Define the enemy object extending pygame.sprite.Sprite
# Instead of a surface, we use an image for a better looking sprite
class Jellyfish(pygame.sprite.Sprite):
    def __init__(self,SCREEN_WIDTH, SCREEN_HEIGHT,gameParams):
        super(Jellyfish, self).__init__()
        self.gameParams = gameParams
        self.surf = pygame.image.load("Resources/jellyfish.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated, as is the speed
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT - 400),
            )
        )
        self.minSpeed = 1 * gameParams.velocity * gameParams.deltaTime
        self.maxSpeed = 3 * gameParams.velocity * gameParams.deltaTime
        self.speed = random.randint(self.minSpeed, self.maxSpeed)
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGTH = SCREEN_HEIGHT
        self.movedUpCounter = 0


    # Move the enemy based on speed
    # Remove it when it passes the left edge of the screen
    def update(self):
        if self.movedUpCounter < 20:
            self.rect.move_ip(0, -self.speed) # Move down
        else:
            self.rect.move_ip(0, self.speed) # Move up
            if self.movedUpCounter > 40:
                self.movedUpCounter = 0

        self.movedUpCounter += 1

        if self.rect.right > self.SCREEN_WIDTH / 1.5: # Make jelly fish stop on the right side of the screen
            self.rect.move_ip(-self.speed, 0)
