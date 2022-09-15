
import os, simpleaudio

# Use a different module for sounds, because the pygame soundsystem didn't work together with  python 2.7.5.
# (which was needed for exypriment...)

# Set up the sounds
class SoundSystem():
    def __init__(self,PATH):

        self.move_up_sound = simpleaudio.WaveObject.from_wave_file("Resources/bubbles.wav")
        self.move_down_sound = simpleaudio.WaveObject.from_wave_file("Resources/bubbles.wav")
     #  self.collision_sound = pygame.mixer.Sound("Collision.ogg")
        self.coin_sound = simpleaudio.WaveObject.from_wave_file("Resources/coin.wav")
        self.playingBubbleSound = self.move_up_sound.play()


    # The bubble sound sounds terrible if they overlap,  first check whether something else is playing. Otherwise you can play the sound
    def playBubbleSound(self,sound):
        if not self.playingBubbleSound.is_playing():
            self.playingBubbleSound = sound.play()


