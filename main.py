# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pygame, random

from gameover import GameOver, PressSpaceToReplay
from startscreen import StartScreen, Fish, FishAdventure


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    path = "/Users/danielle/Documents/"

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

    # Define constants for the screen width and height
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 800


    # Define the Player object extending pygame.sprite.Sprite
    # Instead of a surface, we use an image for a better looking sprite
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super(Player, self).__init__()
            self.surf = pygame.image.load(path + "fish.png").convert()
            self.surf.set_colorkey((0, 0, 0), RLEACCEL)
            self.rect = self.surf.get_rect()

        # Move the sprite based on keypresses
        def update(self, pressed_keys):
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
                channel1.play(move_up_sound)
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)
                channel1.play(move_up_sound)
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

            # Keep player on the screen
            if self.rect.left < 0:
                self.rect.left = 0
            elif self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH
            if self.rect.top <= 0:
                self.rect.top = 0
            elif self.rect.bottom >= SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT

    # Define the enemy object extending pygame.sprite.Sprite
    # Instead of a surface, we use an image for a better looking sprite
    class Enemy(pygame.sprite.Sprite):
        def __init__(self):
            super(Enemy, self).__init__()
            self.surf = pygame.image.load(path + "shark.png").convert()
            self.surf.set_colorkey((0, 0, 0), RLEACCEL)
            # The starting position is randomly generated, as is the speed
            self.rect = self.surf.get_rect(
                center=(
                    random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                    random.randint(0, SCREEN_HEIGHT),
                )
            )
            self.speed = random.randint(5, 15)

        # Move the enemy based on speed
        # Remove it when it passes the left edge of the screen
        def update(self):
            self.rect.move_ip(-self.speed, 0)
            if self.rect.right < 0:
                self.kill()


    class Game():
        def __init__(self):
            self.SCREEN_WIDTH = 1000
            self.SCREEN_HEIGHT = 800



        def run(self):
            print('test')


    def runMainGame():
        gamestate = 'mainloop'
        global bgX_far, bgX2_far, bgX_middle, bgX2_middle, bgX_foreground, bgX2_foreground

        # Make the background move
        bgX_far, bgX2_far = move_background(1.4, background_far.get_width(), bgX_far, bgX2_far)
        bgX_middle, bgX2_middle = move_background(1.8, background_middle.get_width(), bgX_middle, bgX2_middle)
        bgX_foreground, bgX2_foreground = move_background(2, background_foreground.get_width(), bgX_foreground,
                                                          bgX2_foreground)

        screen.fill((0, 0, 0))  # black
        screen.blit(background_far, [bgX_far, 0])
        screen.blit(background_far, [bgX2_far, 0])
        screen.blit(background_middle, [bgX_middle, 20])
        screen.blit(background_middle, [bgX2_middle, 20])
        screen.blit(background_foreground, [bgX_foreground, 40])
        screen.blit(background_foreground, [bgX2_foreground, 40])

        for event in pygame.event.get():
            # Did the user hit a key?
            # print("check1")

            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop
                if event.key == K_ESCAPE:
                    print("quitting")
                    gamestate = 'quitgame'

                if event.type == pygame.QUIT:
                    gamestate = 'quitgame'


            # Should we add a new enemy?
            elif event.type == ADDENEMY:
                # Create the new enemy, and add it to our sprite groups
                new_enemy = Enemy()
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

        # print("check2")
        # Get the set of keys pressed and check for user input
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        # Update the position of our enemies and clouds
        enemies.update()

        # Draw all our sprites
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        # print("check4")

        # Check if any enemies have collided with the player
        if pygame.sprite.spritecollideany(player, enemies):
            # If so, remove the player
            player.kill()
            print("Player killed")

            # Stop any moving sounds and play the collision sound
            move_up_sound.stop()
            move_down_sound.stop()
            collision_sound.play()

            # Stop the loop
            gamestate = 'gameover'
            print("Stopping main loop")

        return gamestate


    def runStartScreen():
        gamestate = 'startscreen'
        startscreen = StartScreen()
        fish = Fish()
        fishadventure_text = FishAdventure()
        screen.blit(startscreen.surf, startscreen.surf_center)
        screen.blit(fish.surf, fish.location)
        screen.blit(fishadventure_text.surf, fishadventure_text.location)

        for event in pygame.event.get():
            if event.type == KEYDOWN:

                # If space to start
                if event.key == K_SPACE:
                    startscreen.kill()
                    gamestate = 'mainloop'

                if event.key == K_ESCAPE:
                    print("quitting")
                    gamestate = 'quitgame'

                if event.type == pygame.QUIT:
                    gamestate = 'quitgame'

        return gamestate


    def runGameOver():
        gamestate = 'gameover'
        gameover = GameOver(path, SCREEN_WIDTH, SCREEN_HEIGHT)
        replay = PressSpaceToReplay(path, SCREEN_WIDTH, SCREEN_HEIGHT)
        screen.blit(gameover.surf, gameover.surf_center)
        screen.blit(replay.surf, replay.surf_center)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    gamestate = 'startscreen'

                if event.key == K_ESCAPE:
                    print("quitting")
                    gamestate = 'quitgame'

                if event.type == pygame.QUIT:
                    gamestate = 'quitgame'

        return gamestate


    def move_background(speed, backgroundWidth, bgX, bgX2):
        # Make the background move
        bgX -= speed  # Move both background images back
        bgX2 -= speed

        if bgX < backgroundWidth * -1:  # If our bg is at the -width then reset its position
            bgX = backgroundWidth

        if bgX2 < backgroundWidth * -1:
            bgX2 = backgroundWidth

        return bgX, bgX2

    def setupBackground(SCREEN_WIDTH,SCREEN_HEIGHT):
        # Setup background
        background_far = pygame.image.load(path + 'far.png')
        background_far = pygame.transform.scale(background_far, (SCREEN_WIDTH, background_far.get_height() * 3))
        bgX_far = 0
        bgX2_far = background_far.get_width()

        background_middle = pygame.image.load(path + 'sand.png')
        background_middle = pygame.transform.scale(background_middle, (SCREEN_WIDTH, SCREEN_HEIGHT - 180))
        bgX_middle = 0
        bgX2_middle = background_middle.get_width()

        background_foreground = pygame.image.load(path + 'foreground-merged.png')
        background_foreground = pygame.transform.scale(background_foreground, (SCREEN_WIDTH + 500, SCREEN_HEIGHT - 160))
        bgX_foreground = 0
        bgX2_foreground = background_foreground.get_width()

        # Initialize
        pygame.mixer.init()  # Setup for sounds, defaults are good
        pygame.init()  # Initialize pygame

        return

    # Setup background
    background_far = pygame.image.load(path + 'far.png')
    background_far = pygame.transform.scale(background_far, (SCREEN_WIDTH, background_far.get_height() * 3))
    bgX_far = 0
    bgX2_far = background_far.get_width()

    background_middle = pygame.image.load(path + 'sand.png')
    background_middle = pygame.transform.scale(background_middle, (SCREEN_WIDTH, SCREEN_HEIGHT - 180))
    bgX_middle = 0
    bgX2_middle = background_middle.get_width()

    background_foreground = pygame.image.load(path + 'foreground-merged.png')
    background_foreground = pygame.transform.scale(background_foreground, (SCREEN_WIDTH + 500, SCREEN_HEIGHT - 160))
    bgX_foreground = 0
    bgX2_foreground = background_foreground.get_width()

    # Initialize
    pygame.mixer.init()  # Setup for sounds, defaults are good
    pygame.init()  # Initialize pygame

    # Screen and clock
    clock = pygame.time.Clock()  # Setup the clock for a decent framerate
    screen = pygame.display.set_mode((SCREEN_WIDTH,
                                      SCREEN_HEIGHT))  # Create the screen object. The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT

    # Create custom events for adding a new enemy and cloud
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 400)

    ADDCLOUD = pygame.USEREVENT + 2
    pygame.time.set_timer(ADDCLOUD, 2000)

    ADDBIGBUBBLE = pygame.USEREVENT + 3
    pygame.time.set_timer(ADDBIGBUBBLE, 3000)

    # Create the sprites
    player = Player()  # Create our 'player'
    enemies = pygame.sprite.Group()  # - enemies is used for collision detection and position updates
    clouds = pygame.sprite.Group()  # - clouds is used for position updates
    bubbles = pygame.sprite.Group()  # Same for bubbles
    all_sprites = pygame.sprite.Group()  # - all_sprites isused for rendering
    all_sprites.add(player)

    # Load and play our background music
    # Sound source: http://ccmixter.org/files/Apoxode/59262
    # License: https://creativecommons.org/licenses/by/3.0/
    # pygame.mixer.music.load("Apoxode_-_Electric_1.mp3")
    # pygame.mixer.music.play(loops=-1)

    # create separate Channel objects for simultaneous playback (or to make sure only 1 sound is playing at a time)
    channel1 = pygame.mixer.Channel(0)  # argument must be int

    # Load all our sound files (Sound sources: Jon Fincher)
    move_up_sound = pygame.mixer.Sound(path + "bubbles.wav")
    move_down_sound = pygame.mixer.Sound(path + "bubbles.wav")
    collision_sound = pygame.mixer.Sound(path + "Collision.ogg")

    # Set the base volume for all sounds
    move_up_sound.set_volume(0.2)
    move_down_sound.set_volume(0.2)
    collision_sound.set_volume(0.5)

    # ========== GAME STATES ==============
    gamestate = 'startscreen'
    run = True
    while run:

        if gamestate == 'startscreen':
            gamestate = runStartScreen()

        elif gamestate == 'mainloop':
            gamestate = runMainGame()

        elif gamestate == 'gameover':
            gamestate = runGameOver()

        elif gamestate == 'quitgame':
            run = False

        # Ensure we maintain a 30 frames per second rate
        clock.tick(30)
        pygame.display.flip()

    # ====== QUIT GAME =======
    pygame.mixer.music.stop()
    pygame.mixer.quit()

    pygame.quit()

