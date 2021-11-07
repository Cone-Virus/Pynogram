import load_image
#Popup buttons
class Button():
    def __init__(self,x,y,image):
        self.image, self.rect = load_image.load_image(image)
        self.rect.topleft = (x,y)
    def draw(self,surface):
        #draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))
