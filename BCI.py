import random

from pygame.locals import (
    K_UP,
    K_DOWN,

)
class BrainInput():
    def __init__(self):
        self.currentInput = 0
        self.previousInput = 0
        self.fakeInput = 0

    # Put value retrieved from Turbo-Satori here
    def getCurrentInput(self):

        input = 0  # random.randint(20, 60)

        return input

    def getKeyboardPressFromBrainInput(self):
        self.previousInput = self.currentInput
        self.currentInput = self.getCurrentInput()

        keyboardPress = self.translateToKeyboardPress(self.currentInput, self.previousInput)

        return keyboardPress

    def translateToKeyboardPress(self, currentInput, previousInput):
        keyboardPress = 0
        if currentInput > previousInput:
            keyboardPress = K_UP
        if currentInput < previousInput:
            keyboardPress = K_DOWN
        if currentInput == previousInput:
            keyboardPress = False

        return keyboardPress
