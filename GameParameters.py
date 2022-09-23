import pygame

# Colours

GOLD = (255, 184, 28)
PINK = (170, 22, 166)

class GameParameters():
    def __init__(self,player,SCREEN_WIDTH,SCREEN_HEIGHT,):

        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT

        # Adjustable parameters
        self.gameTimeCounter_s = 200 # How long you want to one game run to last (in seconds)
        self.useBCIinput = True # If true, then player will be controlled by BCI input instead of keyboard presses
        self.velocity = 1
        self.FPS = 60 # Frame rate. # Defines how often the the while loop is run through. E.g., an FPS of 60 will go through the while loop 60 times per second).
        # Create custom events for adding a new sprites
        self.ADDSHARK = pygame.USEREVENT + 1
        pygame.time.set_timer(self.ADDSHARK, 700) # Define how quickly new sharks are added (e.g., every 1000ms)
        # Create custom events for adding a new sharks
        self.ADDJELLYFISH = pygame.USEREVENT + 2
        pygame.time.set_timer(self.ADDJELLYFISH, 6000) # Define how quickly new jellyfish are added (e.g., every 4000ms)




        # Time
        self.deltaTime = 1

        self.counterText = str('-').rjust(3)
        self.font = pygame.font.SysFont('herculanum', 35, bold=True, )
        self.jellyfishCollectedFont = pygame.font.SysFont('herculanum', 45, bold=True, )
        self.gameTimeCounterText = self.font.render(self.counterText, True, PINK)

        self.nrSharksCollected = 0
        self.nrSharksCollectedText = self.font.render(self.counterText, True, GOLD)

        self.scoreSaved = False

        # Create the sprites
        self.player = player
        print('Player created')
        self.sharks = pygame.sprite.Group()  # - sharks is used for collision detection and position updates
        self.jellyfish = pygame.sprite.Group()  # - enemies is used for collision detection and position updates
        self.all_sprites = pygame.sprite.Group()  # - all_sprites isused for rendering
        self.all_sprites.add(self.player)

        # Counter
        pygame.time.set_timer(pygame.USEREVENT, 1000) # in ms

    def reset(self):
        self.all_sprites.empty()

    def run(self):
        print('test')

