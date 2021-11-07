import pygame
import Button
import get_path

class Tutorial():
    def __init__(self):
        # Back Button
        self.back_button = Button.Button(750, 10, "images/Back-Button.png")

        # Title Header
        font = pygame.font.Font(get_path.get_path("assets/font/freesansbold.ttf"), 60) # Title
        self.text = font.render("How To Play", True, (0,0,0))

        # Tutorial Image
        self.tut = Button.Button(140,200, "images/Tutorial.png") # Loading in as button because im lazy

    def tutScreen(self,surface,mute):
        surface.fill((255,255,255))
        surface.blit(self.text, [300,60])

        # Draw Button
        self.back_button.draw(surface)

        # Draw mute button
        mute.draw(surface)

        # Tutorial Image
        self.tut.draw(surface)

        # Interaction loop
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if e.button == 1:
                    if mute.rect.collidepoint(x, y): # left click on mute music button
                        mute.toggleMusic() # mute/unmute music
                    if self.back_button.rect.collidepoint(x, y): # left click on back button
                        return "Main Menu" # return main menu state
        return "Tutorial"