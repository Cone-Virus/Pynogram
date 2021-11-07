import pygame
import Button
import get_path

class LevelSelect():
    def __init__(self):
        # Difficulty selection buttons
        self.difficulty = ""
        self.size5 = Button.Button(250, 200, "images/size5.png")
        self.size10 = Button.Button(250, 400, "images/size10.png")
        self.size15 = Button.Button(250, 600, "images/size15.png")

        # Level selection buttons
        self.level = ""
        self.level1 = Button.Button(125, 225, "images/level1.png")
        self.level2 = Button.Button(375, 225, "images/level2.png")
        self.level3 = Button.Button(625, 225, "images/level3.png")
        self.level4 = Button.Button(125, 500, "images/level4.png")
        self.level5 = Button.Button(375, 500, "images/level5.png")
        self.level6 = Button.Button(625, 500, "images/level6.png")

        # Solution file name
        self.solnName = ""

    def genSol(self): # Generate Solution
        self.solnName = "levels/" + self.difficulty + "-" + self.level + ".txt"

    def Difficulty(self,surface,mute): # From main to difficulty selection
        surface.fill((255,255,255)) # white background
        mute.draw(surface) # mute button
        font = pygame.font.Font(get_path.get_path("assets/font/freesansbold.ttf"), 60) # Title
        text = font.render("Select Puzzle Size", True, (0,0,0))
        surface.blit(text, [195, 60])

        # Draw Difficulty Buttons
        self.size5.draw(surface)
        self.size10.draw(surface)
        self.size15.draw(surface)

        # Interaction loop
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if e.button == 1:
                    if mute.rect.collidepoint(x, y): # left click on mute music button
                        mute.toggleMusic() # mute/unmute music
                    elif self.size5.rect.collidepoint(x, y): # Selection of levels
                        self.difficulty = "5" # Select level 5
                    elif self.size10.rect.collidepoint(x, y): # Selection of levels
                        self.difficulty = "10" # Select level 10
                    elif self.size15.rect.collidepoint(x, y): # Selection of levels
                        self.difficulty = "15" # Select level 15

    def lvlSelect(self,surface,mute): # From difficulty to selection
        # All the code to display things on the screen goes here
        surface.fill((255,255,255)) # white background
        mute.draw(surface) # mute button

        # Header text
        font = pygame.font.Font(get_path.get_path("assets/font/freesansbold.ttf"), 60)
        text = font.render("Select a Puzzle", True, (0,0,0))
        surface.blit(text, [250, 60])

        # Draw Level buttons
        self.level1.draw(surface)
        self.level2.draw(surface)
        self.level3.draw(surface)
        self.level4.draw(surface)
        self.level5.draw(surface)
        self.level6.draw(surface)

        # Interaction loop
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if e.button == 1:
                    if mute.rect.collidepoint(x, y): # left click on mute music button
                        mute.toggleMusic() # mute/unmute music
                    elif self.level1.rect.collidepoint(x, y):
                        self.level = "1"
                        self.genSol()
                    elif self.level2.rect.collidepoint(x, y):
                        self.level = "2"
                        self.genSol()
                    elif self.level3.rect.collidepoint(x, y):
                        self.level = "3"
                        self.genSol()
                    elif self.level4.rect.collidepoint(x, y):
                        self.level = "4"
                        self.genSol()
                    elif self.level5.rect.collidepoint(x, y):
                        self.level = "5"
                        self.genSol()
                    elif self.level6.rect.collidepoint(x, y):
                        self.level = "6"
                        self.genSol()

