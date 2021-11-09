import pygame
import Button
import get_path

class Tutorial():
    def __init__(self):
        # Back Button
        self.back_button = Button.Button(790, 20, "images/Back-Button.png")

        # Tutorial Image
        self.tut = Button.Button(140,200, "images/Tutorial.png") # Loading in as button because im lazy

    def tutScreen(self,surface,mute,themeMgr):
        # Title Header
        font = pygame.font.Font(get_path.get_path("assets/font/freesansbold.ttf"), 60) # Title
        self.text = font.render("How To Play", True, themeMgr.getFontColor())
        surface.blit(self.text, [300,60])

        # Draw Button
        self.back_button.draw(surface,themeMgr)

        # Draw mute button
        mute.draw(surface,themeMgr)

        # Tutorial Image
        self.tut.draw(surface,themeMgr)

        # Interaction loop
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit() # Prevents error message when quitting

            if e.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if e.button == 1:
                    if mute.rect.collidepoint(x, y): # left click on mute music button
                        mute.toggleMusic(themeMgr) # mute/unmute music
                    if self.back_button.rect.collidepoint(x, y): # left click on back button
                        return "Main Menu" # return main menu state
        return "Tutorial"
