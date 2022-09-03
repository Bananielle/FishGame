# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pygame, random

from MainGame_background import MainGame_background
from gameover import GameOver, PressSpaceToReplay
from startscreen import StartScreen, Fish, FishAdventure


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


    def run():

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
                self.minSpeed = 5
                self.maxSpeed = 15
                self.speed = random.randint(self.minSpeed, self.maxSpeed)

            def increaseDifficulty(self, increaseSpeedBy):
                self.speed = random.randint(5 + increaseSpeedBy, 15 + increaseSpeedBy)

            # Move the enemy based on speed
            # Remove it when it passes the left edge of the screen
            def update(self):
                self.rect.move_ip(-self.speed, 0)
                if self.rect.right < 0:
                    self.kill()

        class GameParameters():
            def __init__(self):
                self.SCREEN_WIDTH = 1000
                self.SCREEN_HEIGHT = 800
                self.difficultyCounter = 0
                self.maxSpeed = 15
                self.minSpeed = 5
                self.timer = 400
                self.gameTimeCounter = 0
                self.counterText = str('0').rjust(3)
                self.font = pygame.font.SysFont('herculanum', 35, bold=True, )
                self.gameCounterText = self.font.render(self.counterText, True, (255, 184, 28))

                self.scoreSaved = False

                # Create custom events for adding a new enemy and cloud
                self.ADDENEMY = pygame.USEREVENT + 1
                pygame.time.set_timer(self.ADDENEMY, 400)

                # Create the sprites
                self.player = Player()  # Create our 'player'
                print('Player created')
                self.enemies = pygame.sprite.Group()  # - enemies is used for collision detection and position updates
                self.all_sprites = pygame.sprite.Group()  # - all_sprites isused for rendering
                self.all_sprites.add(self.player)

                # Counter
                pygame.time.set_timer(pygame.USEREVENT, 1000)

            def reset(self):
                self.all_sprites.empty()

            def run(self):
                print('test')

        class Scoreboard():
            def __init__(self):
                self.scoresList = []
                self.font = pygame.font.SysFont('herculanum', 35, bold=True, )

                self.scores_string = ' '
                self.scores_text = self.font.render(self.scores_string, True, (255, 184, 28))

            def addScoretoScoreBoard(self, score):
                if not gameParams.scoreSaved:
                    self.scoresList.append(score)
                    gameParams.scoreSaved = True  # This will reset when the player goes back to the start screen
                    print('Score ', score, ' saved to score list. Is now: ', str(self.scoresList))

            def displayScoreboard(self):

                text1 = 'Scoreboard'
                text2 = '(seconds lasted)'
                scoreboard = self.font.render(text1, True, (255, 184, 28))
                secondsLasted = self.font.render(text2, True, (255, 184, 28))

                screen.blit(scoreboard,
                            ((SCREEN_WIDTH / 2) - (SCREEN_WIDTH * 0.11), (SCREEN_HEIGHT / 2) - (SCREEN_HEIGHT * 0.40)))
                # screen.blit(secondsLasted,((SCREEN_WIDTH / 2) - (SCREEN_WIDTH * 0.14), (SCREEN_HEIGHT / 2) - (SCREEN_HEIGHT * 0.40)+30))

                currentScoreFound = False
                newPosition = 30
                count = 1
                sortedScores = sorted(self.scoresList, reverse=True)
                for score in sortedScores:
                    count_str = str(count) + '.'
                    if score == gameParams.gameTimeCounter and not currentScoreFound:
                        scores_text = self.font.render(str(score) + ' seconds', True, (255, 0, 28))
                        count_text = self.font.render(count_str, True, (255, 0, 28))
                        currentScoreFound = True
                    else:
                        scores_text = self.font.render(str(score) + ' seconds', True, (255, 184, 28))
                        count_text = self.font.render(count_str, True, (255, 184, 28))
                    screen.blit(count_text,
                                ((SCREEN_WIDTH / 2.2) - 80, (SCREEN_HEIGHT / 2) - (SCREEN_HEIGHT * 0.35) + newPosition))
                    screen.blit(scores_text,
                                ((SCREEN_WIDTH / 2.2), (SCREEN_HEIGHT / 2) - (SCREEN_HEIGHT * 0.35) + newPosition))
                    newPosition += 30
                    count += 1
                    # print('score ', score, ' printed')

        def displaySeaBackgroundsOnScreen():

            screen.fill((0, 0, 0))  # black
            screen.blit(mainGame_background.background_far, [mainGame_background.bgX_far, 0])
            screen.blit(mainGame_background.background_far, [mainGame_background.bgX2_far, 0])
            screen.blit(mainGame_background.background_middle, [mainGame_background.bgX_middle, 20])
            screen.blit(mainGame_background.background_middle, [mainGame_background.bgX2_middle, 20])
            screen.blit(mainGame_background.background_foreground, [mainGame_background.bgX_foreground, 40])
            screen.blit(mainGame_background.background_foreground, [mainGame_background.bgX2_foreground, 40])

            # return mainGame_background

        def didPlayerPressQuit(gamestate, event):

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    gamestate = 'quitgame'
                    print('Going to state: ' + gamestate)

            elif event.type == pygame.QUIT:
                gamestate = 'quitgame'
                print('Going to state: ' + gamestate)

            return gamestate

        def runMainGame():
            gamestate = 'mainloop'

            mainGame_background.updateBackGrounds()
            displaySeaBackgroundsOnScreen()

            # mainGame_background.updateBackGrounds()
            #
            # screen.fill((0, 0, 0))  # black
            # screen.blit(mainGame_background.background_far, [mainGame_background.bgX_far, 0])
            # screen.blit(mainGame_background.background_far, [mainGame_background.bgX2_far, 0])
            # screen.blit(mainGame_background.background_middle, [mainGame_background.bgX_middle, 20])
            # screen.blit(mainGame_background.background_middle, [mainGame_background.bgX2_middle, 20])
            # screen.blit(mainGame_background.background_foreground, [mainGame_background.bgX_foreground, 40])
            # screen.blit(mainGame_background.background_foreground, [mainGame_background.bgX2_foreground, 40])

            for event in pygame.event.get():
                # Did the user hit a key?
                # print("check1")

                # Show the player how much time as passed
                if event.type == pygame.USEREVENT:
                    gameParams.gameTimeCounter += 1
                    text = str(gameParams.gameTimeCounter).rjust(3)
                    gameParams.gameCounterText = gameParams.font.render(text, True, (255, 184, 28))

                    print(text)

                gamestate = didPlayerPressQuit(gamestate, event)

                # Should we add a new enemy?
                if event.type == gameParams.ADDENEMY:
                    # Create the new enemy, and add it to our sprite groups
                    new_enemy = Enemy()
                    gameParams.enemies.add(new_enemy)
                    gameParams.all_sprites.add(new_enemy)

                    # Increase difficulty the longer the player is in the game
                    if gameParams.difficultyCounter > 150:
                        gameParams.difficultyCounter = 0
                        gameParams.maxSpeed = gameParams.maxSpeed + 1
                        gameParams.minSpeed = gameParams.minSpeed + 1
                        if gameParams.maxSpeed > 30:
                            gameParams.maxSpeed = 30
                            gameParams.minSpeed = 28

                        new_enemy.speed = random.randint(gameParams.minSpeed, gameParams.maxSpeed)
                        gameParams.timer = gameParams.timer - 5
                        pygame.time.set_timer(gameParams.ADDENEMY, gameParams.timer)
                        print('Main game: Difficulty updated. Minspeed = ', gameParams.maxSpeed, ', maxspeed = ',
                              gameParams.minSpeed)

            # print("check2")
            # Get the set of keys pressed and check for user input
            pressed_keys = pygame.key.get_pressed()
            gameParams.player.update(pressed_keys)

            # Update the position of our enemies and clouds
            gameParams.enemies.update()

            # Draw all our sprites
            for entity in gameParams.all_sprites:
                screen.blit(entity.surf, entity.rect)

                gameParams.difficultyCounter = gameParams.difficultyCounter + 1;

            # print("check4")

            # Draw counter text
            screen.blit(gameParams.gameCounterText, (SCREEN_WIDTH - 70, 20))

            # Check if any enemies have collided with the player
            if pygame.sprite.spritecollideany(gameParams.player, gameParams.enemies):
                # If so, remove the player
                gameParams.player.kill()
                print("Main game: Player killed")

                # Stop any moving sounds and play the collision sound
                move_up_sound.stop()
                move_down_sound.stop()
                collision_sound.play()

                # Stop the loop
                gamestate = 'gameover'
                print("Main game: Stopping main loop. Going to gamestate: " + gamestate)

            return gamestate

        def runStartScreen():
            gamestate = 'startscreen'
            screen.fill([0, 0, 0])  # Set black background
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
                        gamestate = 'startNewGame'
                        print('Going to state: ' + gamestate)

                    gamestate = didPlayerPressQuit(gamestate, event)

            return gamestate

        def runGameOver():
            gamestate = 'gameover'
            gameover = GameOver(path, SCREEN_WIDTH, SCREEN_HEIGHT)
            replay = PressSpaceToReplay(path, SCREEN_WIDTH, SCREEN_HEIGHT)
            screen.blit(gameover.surf, gameover.surf_center)
            screen.blit(replay.surf, replay.surf_center)

            # Save the score for the player
            scoreboard.addScoretoScoreBoard(gameParams.gameTimeCounter)

            for event in pygame.event.get():

                if event.type == KEYDOWN:

                    if event.key == K_SPACE:
                        gamestate = 'scoreboard'
                        print('Going to state: ' + gamestate)

                        # Reset game parameters if you want to restart a game
                        gameParams.reset()

                gamestate = didPlayerPressQuit(gamestate, event)

            return gamestate

        def runScoreboard():
            gamestate = 'scoreboard'

            displaySeaBackgroundsOnScreen()
            scoreboard.displayScoreboard()

            for event in pygame.event.get():
                if event.type == KEYDOWN:

                    if event.key == K_SPACE:
                        gamestate = 'startscreen'
                        print('Going to state: ' + gamestate)

                        # Reset game parameters if you want to restart a game
                        gameParams.reset()
                        # del mainGame_background

                gamestate = didPlayerPressQuit(gamestate, event)

            return gamestate

        def startANewGame():
            print('Starting a new game.')
            gamestate = 'mainloop'
            print('Going to state: ' + gamestate)

            return gamestate, GameParameters(), MainGame_background()  # Reinitialize game parameters and background

        # INITIALIZE MAIN GAME SCREEN

        # Initialize
        pygame.mixer.init()  # Setup for sounds, defaults are good
        pygame.init()  # Initialize pygame

        # Clock
        clock = pygame.time.Clock()  # Setup the clock for a decent framerate

        # Screen
        SURFACE = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE
        screen = pygame.display.set_mode((SCREEN_WIDTH,
                                          SCREEN_HEIGHT),
                                         SURFACE)  # Create the screen object. The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT

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

        gamestate, gameParams, mainGame_background = startANewGame()
        scoreboard = Scoreboard()

        # START OF A NEW GAME (needs to happen every time a new game is started)

        # ========== GAME STATES ==============
        gamestate = 'startscreen'
        run = True
        while run:

            if gamestate == 'startscreen':
                gamestate = runStartScreen()

            if gamestate == 'startNewGame':
                gamestate, gameParams, mainGame_background = startANewGame()

            elif gamestate == 'mainloop':
                gamestate = runMainGame()

            elif gamestate == 'gameover':
                gamestate = runGameOver()

            elif gamestate == 'scoreboard':
                gamestate = runScoreboard()

            elif gamestate == 'quitgame':
                run = False

            # Ensure we maintain a 30 frames per second rate
            clock.tick(50)
            pygame.display.flip()

        # ====== QUIT GAME =======
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        print('quitting game')

        pygame.quit()


    run()  # Run the main script
