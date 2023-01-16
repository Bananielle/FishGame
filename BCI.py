import pygame
import _turbosatorinetworkinterface as tsi  # handles getting data from TSI

from pygame.locals import (
    K_UP,
    K_DOWN,

)

class BCI():
    def __init__(self,SCREEN_HEIGHT):
        self.currentInput = 0
        self.previousInput = 0
        self.fakeInput = 0
        self.TSIconnectionFound = True
        self.timeBetweenSamples_ms = 100000
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.inputMultiplier = 0;

        # Look for a connection to turbo-satori
        try:
            self.tsi = tsi.TurbosatoriNetworkInterface("127.0.0.1", 55556)
        except:
            # None found? Let the user know
            self.TSIconnectionFound = False
            print("Turbo satori connection not found.")

        if self.TSIconnectionFound:
            self.timeBetweenSamples_ms = self.establishTimeInBetweenSamples()

        self.GET_TURBOSATORI_INPUT = pygame.USEREVENT + 5
        pygame.time.set_timer(self.GET_TURBOSATORI_INPUT, self.timeBetweenSamples_ms) # I have to give it integers...

    def getCurrentInput(self):

        if self.TSIconnectionFound:
            currentTimePoint = self.tsi.get_current_time_point()[0]
            Selected = self.tsi.get_selected_channels()[0]
            oxy = self.tsi.get_data_oxy(Selected[0], currentTimePoint - 1)[0]
            input = oxy

            input = round(oxy,4)
            print("Current time point: " + str(currentTimePoint), ", selected channels: " + str(Selected) + " , oxy: " + str(input))



        else:
            input = 0

        return input

    def getKeyboardPressFromBrainInput(self):
        self.previousInput = self.currentInput
        self.currentInput = self.getCurrentInput()

        keyboardPress = self.translateToKeyboardPress(self.currentInput, self.previousInput)

        return keyboardPress

    def translateToKeyboardPress(self, currentInput, previousInput):
        keyboardPress = 0
        if currentInput > 0:
            if currentInput > previousInput:
                keyboardPress = K_UP
        if currentInput < previousInput:
            keyboardPress = K_DOWN
        if currentInput == previousInput:
            keyboardPress = False

        return keyboardPress

    def getMaxInput(self, ):
        maxInput = 0.2
        # if 0.2 is the max that oxy will give and screen size is 1000, and a step is 5, then I have 200 steps for a screen.
        # So 1000/0.2 = 5000, meaning I have to multiply everything by 5000 to get to max screen size.

        return maxInput

    def calculateInputMultiplier(self):
        max_BCI_input = self.getMaxInput()

        inputMultiplier = self.SCREEN_HEIGHT / max_BCI_input

        return inputMultiplier


    def calculateNrOfStepsToTake(self):
        # Translate brain input to screen size

        inputMultiplier = self.calculateInputMultiplier()

        translated_BCI_input_current = self.currentInput * inputMultiplier
        translated_BCI_input_previous = self.previousInput * inputMultiplier
        numberOfStepsForFishToTake = translated_BCI_input_current - translated_BCI_input_previous

        return numberOfStepsForFishToTake

    # with current data its 7.8125 samples per second. So a sample every 128ms.
    def establishTimeInBetweenSamples(self):
        samplingRate = self.tsi.get_sampling_rate()
        timeBetweenSamples_ms = int(1000 / samplingRate[0])
        print("Sampling rate = "+  str(self.tsi.get_sampling_rate()) + ", so " + str(timeBetweenSamples_ms) + "ms inbetween samples.")

        return timeBetweenSamples_ms