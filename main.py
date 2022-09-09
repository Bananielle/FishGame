# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pygame, random

from GameParameters import GameParameters
from SeaBackground import MainGame_background
from Sharks import Shark
from SoundSystem import SoundSystem
from gameover import GameOver, PressSpaceToReplay
from StartScreenPics import PressSpace, Fish, FishAdventure
from MainPlayer import MainPlayer


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Starting up fish game...')

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

    PATH = "/Users/danielle/PycharmProjects/FishGame/sounds_pics/"

    # Colours
    GOLD = (255, 184, 28)
    PINK = (170,22,166)

    # Used to cycle through different game states with a statemachine
    class GameStates:
        STARTSCREEN = 'StartScreen'
        STARTNEWGAME = 'StartNewGame'
        MAINGAME = 'MainGame'
        GAMEOVER = 'GameOver'
        SCOREBOARD = 'Scoreboard'
        QUITGAME = 'QuitGame'

        def setGameState(self,gamestate):
            print('Going to state: ' + gamestate)
            return gamestate

    class Scoreboard():
        def __init__(self):
            self.scoresList = []
            self.font = pygame.font.SysFont('herculanum', 35, bold=True, )

        def addScoretoScoreBoard(self, score):
            if not gameParams.scoreSaved:
                self.scoresList.append(score)
                gameParams.scoreSaved = True  # This will reset when the player goes back to the start screen
                print('Score ', score, ' saved to score list. Is now: ', str(self.scoresList))

        def makePinkFont(self, string):
            text = self.font.render(string, True, PINK) # Pink colour
            return text

        def displayScoreboard(self):

            scoreboard = self.makePinkFont('Scoreboard')
            screen.blit(scoreboard, ((SCREEN_WIDTH / 2) - (SCREEN_WIDTH * 0.11), (SCREEN_HEIGHT / 2) - (SCREEN_HEIGHT * 0.40)))

            currentScoreAlreadyDisplayed = False
            newPosition = 30
            count = 1
            sortedScores = sorted(self.scoresList, reverse=True)

            # Put each score on the screen in descending order
            for score in sortedScores:
                count_str = str(count) + '.'
                if score == gameParams.nrSharksCollected and not currentScoreAlreadyDisplayed: # Colour the currently achieved score GOLD
                    scores_text = self.font.render(str(score) + ' sharks', True, GOLD)
                    count_text = self.font.render(count_str, True, GOLD)
                    currentScoreAlreadyDisplayed = True
                else:
                    scores_text = self.makePinkFont(str(score) + ' sharks')
                    count_text = self.makePinkFont(count_str)

                # Put score on screen
                screen.blit(count_text,
                            ((SCREEN_WIDTH / 2.2) - 80, (SCREEN_HEIGHT / 2) - (SCREEN_HEIGHT * 0.35) + newPosition))
                screen.blit(scores_text,
                            ((SCREEN_WIDTH / 2.2), (SCREEN_HEIGHT / 2) - (SCREEN_HEIGHT * 0.35) + newPosition))
                newPosition += 30
                count += 1
                # print('score ', score, ' printed')

    # GAME STATE FUNCTIONS
    def startANewGame():
        print('Starting a new game.')
        gamestate = GameState.setGameState(GameState.MAINGAME)

        player = MainPlayer(SCREEN_WIDTH,SCREEN_HEIGHT,PATH, soundSystem)

        gameParameters = GameParameters(player,SCREEN_WIDTH,SCREEN_HEIGHT,PATH)

        mainGameBackGround = MainGame_background(SCREEN_WIDTH,SCREEN_HEIGHT,PATH)

        return gamestate, gameParameters, mainGameBackGround  # Reinitialize game parameters and background

    def runStartScreen():
        gamestate = GameState.STARTSCREEN
        screen.fill([0, 0, 0])  # Set black background
        startscreen = PressSpace(SCREEN_WIDTH,SCREEN_HEIGHT,PATH)
        fish = Fish(SCREEN_WIDTH,SCREEN_HEIGHT,PATH)
        fishadventure_text = FishAdventure(SCREEN_WIDTH,SCREEN_HEIGHT,PATH)
        screen.blit(startscreen.surf, startscreen.surf_center)
        screen.blit(fish.surf, fish.location)
        screen.blit(fishadventure_text.surf, fishadventure_text.location)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                # If space to start
                if event.key == K_SPACE:
                    startscreen.kill()
                    gamestate = GameState.setGameState(GameState.STARTNEWGAME)

                gamestate = didPlayerPressQuit(gamestate, event)

        return gamestate

    def runMainGame():
        gamestate = GameState.MAINGAME

        mainGame_background.updateBackGrounds()
        displaySeaBackgroundsOnScreen()

        for event in pygame.event.get():
            # Did the user hit a key?
            # print("check1")

            # Show the player how much time as passed
            if event.type == pygame.USEREVENT:
                if (gameParams.gameTimeCounter_s == 0):
                    gamestate = GameState.GAMEOVER
                    gameParams.player.kill()
                else:
                    gameParams.gameTimeCounter_s -= 1
                    text = str(gameParams.gameTimeCounter_s).rjust(3)
                    gameParams.gameTimeCounterText = scoreboard.makePinkFont(text)
                    print(text)

            gamestate = didPlayerPressQuit(gamestate, event)

            # Should we add a new enemy?
            if event.type == gameParams.ADDSHARK:
                # Create the new enemy, and add it to our sprite groups
                new_shark = Shark(SCREEN_WIDTH,SCREEN_HEIGHT,PATH)
                gameParams.enemies.add(new_shark)
                gameParams.all_sprites.add(new_shark)

                # Increase difficulty the longer the player is in the game
                if gameParams.difficultyCounter > 150:
                    gameParams.difficultyCounter = 0
                    gameParams.maxSpeed = gameParams.maxSpeed + 1
                    gameParams.minSpeed = gameParams.minSpeed + 1
                    if gameParams.maxSpeed > 30:
                        gameParams.maxSpeed = 30
                        gameParams.minSpeed = 28

                    new_shark.speed = random.randint(gameParams.minSpeed, gameParams.maxSpeed)
                    gameParams.timer_ms = gameParams.timer_ms - 5
                    pygame.time.set_timer(gameParams.ADDSHARK, gameParams.timer_ms)
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

        # Check if any enemies have collided with the player
        for shark in gameParams.enemies:
            if shark.rect.colliderect(gameParams.player.rect):
                shark.kill()
                soundSystem.coin_sound.play()
                gameParams.nrSharksCollected += 1
                # Show the player how much coins have been collected
                text = str(gameParams.nrSharksCollected).rjust(3)
                gameParams.nrSharksCollectedText = gameParams.font.render(text, True, GOLD)

        # Draw game time counter text
        screen.blit(gameParams.gameTimeCounterText, (SCREEN_WIDTH - 70, 20))
        screen.blit(gameParams.nrSharksCollectedText, (SCREEN_WIDTH - 70, 50))

        return gamestate

    def runGameOver():
        gamestate = GameState.GAMEOVER
        gameover = GameOver(PATH, SCREEN_WIDTH, SCREEN_HEIGHT)
        replay = PressSpaceToReplay(PATH, SCREEN_WIDTH, SCREEN_HEIGHT)
        screen.blit(gameover.surf, gameover.surf_center)
        screen.blit(replay.surf, replay.surf_center)

        # Save the score for the player
        scoreboard.addScoretoScoreBoard(gameParams.nrSharksCollected)

        for event in pygame.event.get():

            if event.type == KEYDOWN:

                if event.key == K_SPACE:
                    gamestate = GameState.setGameState(GameState.SCOREBOARD)

                    # Reset game parameters if you want to restart a game
                    gameParams.reset()

            gamestate = didPlayerPressQuit(gamestate, event)

        return gamestate

    def runScoreboard():
        gamestate = GameState.SCOREBOARD

        displaySeaBackgroundsOnScreen()
        replay = PressSpaceToReplay(PATH, SCREEN_WIDTH, SCREEN_HEIGHT)
        screen.blit(replay.surf, replay.surf_center)
        scoreboard.displayScoreboard()

        for event in pygame.event.get():
            if event.type == KEYDOWN:

                if event.key == K_SPACE:
                    gamestate = GameState.setGameState(GameState.STARTSCREEN)

            gamestate = didPlayerPressQuit(gamestate, event)

        return gamestate

    # OTHER FUNCTIONS
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
                gamestate = GameState.setGameState(GameState.QUITGAME)

        if event.type == pygame.QUIT:
            gamestate = GameState.setGameState(GameState.QUITGAME)


        return gamestate

        # Define constants for the screen width and height

    # INITIALIZE MAIN GAME SCREEN
    pygame.init()  # Initialize pygame

    infoObject = pygame.display.Info()
    # pygame.display.set_mode((infoObject.current_w, infoObject.current_h))

    SCREEN_WIDTH = infoObject.current_w
    SCREEN_HEIGHT = infoObject.current_h
    print('Screen width = ' + str(SCREEN_WIDTH) + ', screen height = ' + str(SCREEN_HEIGHT))

    # Clock
    clock = pygame.time.Clock()  # Setup the clock for a decent framerate

    # Screen
    SURFACE = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE
    # Create the screen object. The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.FULLSCREEN) # WARNING: WITH fullscreen using an external screen may cause problems (tip: it helps if you don't have pycharm in fullscreen already)

    # Setup sounds
    pygame.mixer.init()  # Setup for sounds, defaults are good
    soundSystem = SoundSystem(PATH)

    # Set up gamestates to cycle through in main loop
    GameState = GameStates()

    # Make a scoreboard (will remain throughout the game)
    scoreboard = Scoreboard()

    # Set up a new game (will be refreshed after every replay)
    gamestate, gameParams, mainGame_background = startANewGame()


    # ========== GAME STATE MACHINE ==============
    gamestate = GameState.STARTSCREEN
    run = True
    while run:

        if gamestate == GameState.STARTSCREEN:
            gamestate = runStartScreen()

        if gamestate == GameState.STARTNEWGAME:
            gamestate, gameParams, mainGame_background = startANewGame()

        elif gamestate == GameState.MAINGAME:
            gamestate = runMainGame()

        elif gamestate == GameState.GAMEOVER:
            gamestate = runGameOver()

        elif gamestate == GameState.SCOREBOARD:
            gamestate = runScoreboard()

        elif gamestate == GameState.QUITGAME:
            run = False # quit the while loop

        # Ensure we maintain a 30 frames per second rate
        clock.tick(50)
        pygame.display.flip()


    # ====== QUIT GAME =======
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    print('quitting game')

    pygame.quit()
