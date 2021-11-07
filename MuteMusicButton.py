import Button
import pygame
import load_image

# Button for muting/unmuting the music
class MuteMusicButton(Button.Button):
    # Keeps track of whether music is on or not
    musicEnabled = True

    # Constructor
    def __init__(self, x, y, image):
        super(MuteMusicButton, self).__init__(x, y, image)
        self.musicEnabled = True

    # Change sprite and toggle music based on current state
    def toggleMusic(self):
        if self.musicEnabled: # music on -> mute music
            self.musicEnabled = False
            pygame.mixer.music.pause()
            self.image, self.rect = load_image.load_image("images/music-off.bmp")
            self.rect.topleft = 790, 800 # Position on screen
        else: # music off -> turn on music
            self.musicEnabled = True
            pygame.mixer.music.unpause()
            self.image, self.rect = load_image.load_image("images/music-on.bmp")
            self.rect.topleft = 790, 800 # Position on screen
