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
    def toggleMusic(self, themeMgr):
        if self.musicEnabled: # music on -> mute music
            self.musicEnabled = False
            pygame.mixer.music.pause()
            self.image, self.rect = load_image.load_image(themeMgr.getFileName("music_off.png"))
        else: # music off -> turn on music
            self.musicEnabled = True
            pygame.mixer.music.unpause()
            self.image, self.rect = load_image.load_image(themeMgr.getFileName("music_on.png"))

        self.rect.topleft = self.coords # restore correct position on screen


    def draw(self,surface,themeMgr):

        # if image needs to be changed
        if self.musicEnabled:
            tempName = "music_on.png"
        else:
            tempName = "music_off.png"

        if self.filename != themeMgr.getFileName(tempName):
            self.filename = themeMgr.getFileName(tempName)
            self.image, self.rect = load_image.load_image(self.filename)
            self.rect.topleft = self.coords

        #draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))
