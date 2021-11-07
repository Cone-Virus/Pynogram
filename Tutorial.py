import pygame
import Button

class Tutorial():
    def __init__(self):
        # Back Button
        self.back_button = Button.Button(10, 750, "images/Back-Button.png")

        # Title Header
        font = pygame.font.Font('assets/font/freesansbold.ttf', 60) # Title
        self.text = font.render("Tutorial", True, (0,0,0))

        # Tutorial Image
        self.tut = Button.Button(140,200, "images/Tutorial.png") # Loading in as button because im lazy

    def tutScreen(self,surface):
        surface.fill((255,255,255))
        surface.blit(self.text, [350,60])

        # Draw Button
        self.back_button.draw(surface)

        # Tutorial Image
        self.tut.draw(surface)

        # Interaction loop
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if e.button == 1:
                    if self.back_button.rect.collidepoint(x, y): # left click on back button
                        return "Board" # return board state
        return "Tutorial"
