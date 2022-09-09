import pygame

# Set up the sounds
class SoundSystem():
    def __init__(self,PATH):
        # create separate Channel objects for simultaneous playback (or to make sure only 1 sound is playing at a time)
        self.channel1 = pygame.mixer.Channel(0)  # argument must be int
        # Load all our sound files (Sound sources: Jon Fincher)
        self.move_up_sound = pygame.mixer.Sound(PATH + "bubbles.wav")
        self.move_down_sound = pygame.mixer.Sound(PATH + "bubbles.wav")
        self.collision_sound = pygame.mixer.Sound(PATH + "Collision.ogg")
        self.coin_sound = pygame.mixer.Sound(PATH + "coin.wav")

        # Set the base volume for all sounds
        self.move_up_sound.set_volume(0.2)
        self.move_down_sound.set_volume(0.2)
        self.collision_sound.set_volume(0.5)
        self.coin_sound.set_volume(0.2)
