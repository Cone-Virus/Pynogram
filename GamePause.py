import pygame
import Button
import get_path

class Pause():
    def __init__(self):
        # Buttons
        self.main_button = Button.Button(275,250, "images/pause-main.png")
        self.quit_button = Button.Button(275,450, "images/pause-quit.png")
        self.resume = Button.Button(10,10, "images/resume.png")

        # Title Header
        font = pygame.font.Font(get_path.get_path("assets/font/freesansbold.ttf"), 60) # Title
        self.text = font.render("Game Paused", True, (0,0,0))

    def pauseScreen(self,surface,mute):
        surface.fill((255,255,255))
        surface.blit(self.text, [250,60])

        # Draw Button
        self.main_button.draw(surface)
        self.quit_button.draw(surface)
        self.resume.draw(surface)

        # Draw mute button
        mute.draw(surface)

        # Interaction loop
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if e.button == 1:
                    if mute.rect.collidepoint(x, y): # left click on mute music button
                        mute.toggleMusic() # mute/unmute music
                    elif self.resume.rect.collidepoint(x, y): # left click on back button
                        return "Resume" # resume game
                    elif self.main_button.rect.collidepoint(x, y): 
                        return "Pause Main" # Pause main
                    elif self.quit_button.rect.collidepoint(x, y):
                        pygame.quit()
                        exit()
        return "Pause"