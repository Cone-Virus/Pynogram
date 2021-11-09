import load_image
#Popup buttons
class Button():
    def __init__(self,x,y,image):
        # save the filename and coordinates to use when updating
        self.defFilename = image[7:] # default, doesn't change (remove prefix of "images/")
        self.filename = image # changes when theme changes (light/dark mode)
        self.coords = x,y

        self.image, self.rect = load_image.load_image(self.filename)
        self.rect.topleft = self.coords

    def draw(self,surface,themeMgr):

        # if image needs to be changed
        if self.filename != themeMgr.getFileName(self.defFilename):
            self.filename = themeMgr.getFileName(self.defFilename)
            self.image, self.rect = load_image.load_image(self.filename)
            self.rect.topleft = self.coords

        #draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))
