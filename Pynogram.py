import os
import pygame
import math
from sys import exit

# Classes from other files
import Board
import Timer
import Button
import ClearButton
import CheckPuzzleButton
import MuteMusicButton
import Tutorial
import LevelSelect
import GamePause
import ThemeMgr

# Functions from other files
import load_image
import blink_anim
import get_path

def main():
    themeMgr = ThemeMgr.ThemeMgr(False) # starts in light mode
    clock = pygame.time.Clock()
    screen = pygame.init()
    surface = pygame.display.set_mode((900,900))
    pygame.display.set_caption("Pynogram")
    surface.fill(themeMgr.getBgColor())
    level = LevelSelect.LevelSelect()
    timer = Timer.Timer()
    board = Board.Board()
    tutorial = Tutorial.Tutorial()
    pause = GamePause.Pause()

    # Determines whether user can edit grid (including clear grid)
    # Check solution is also disabled; since user can't modify grid, result of check won't change
    # This is false when:
    # (1) User has checked their solution and is correct (completed the puzzle)
    # (2) User has checked their solution and is wrong, but chooses to see solution
    # (3) User is not on the board (ex. popup is covering it, different menu)
    canEditGrid = True
    solCorrect = False
    #Used when puzzle incorrect, prevents game from continuing until user selects to try again or give up

    # Set up clear button, check button, mute music button
    clearButton = ClearButton.ClearButton(725, 120, "images/clear.png")
    checkPuzzleButton = CheckPuzzleButton.CheckPuzzleButton(325, 800, "images/check.png")
    muteMusicButton = MuteMusicButton.MuteMusicButton(790,800,"images/music_on.png")

    # Tutorial Button
    tut = Button.Button(250,410, "images/Tutorial-Button.png")

    # Pause Button
    pauseB = Button.Button(30,30, "images/Pause-Button.png")

    # Theme Toggle button
    themeToggle = Button.Button(35,780,"images/theme_toggle.png")

    # Popup buttons
    puzzleComplete = Button.Button(50,115, "images/puzzleComplete.png")
    pcMainMenu = Button.Button(275,495, "images/mainmenu.png")
    puzzleIncorrect = Button.Button(50,115, "images/incorrect.png")
    tryAgain = Button.Button(300,420, "images/tryAgain.png")
    showSolution = Button.Button(300, 510, "images/showSolution.png")

    # Main menu buttons
    quitGame = Button.Button(300, 590, "images/quit.png")
    startGame = Button.Button (170, 200, "images/startGame.png")

    blinkSoln = False # animation when showing solution

    # Load song
    pygame.mixer.music.load(get_path.get_path("assets/music/Arpent.wav"))
    pygame.mixer.music.play(-1) # loop indefinitely

    #Used to prevent interaction with puzzle while popup is active
    gameState = 0

    page = "Main Menu" # FIXME - transition testing

    notNew = True

    while True:
        clock.tick(60) # 60 fps

        surface.fill(themeMgr.getBgColor()) # background, needed for all pages

        if page == "Main Menu":
            muteMusicButton.draw(surface,themeMgr) # mute button
            tut.draw(surface,themeMgr) # Tutorial Button
            themeToggle.draw(surface,themeMgr) # Theme Toggle Button

            # Title text
            font = pygame.font.Font(get_path.get_path('assets/font/freesansbold.ttf'), 70)
            text = font.render("Pynogram", True, themeMgr.getFontColor())
            surface.blit(text, [280, 40])

            # buttons
            startGame.draw(surface,themeMgr)
            quitGame.draw(surface,themeMgr)

        elif page == "Difficulty Selection":
            if level.difficulty == "":
                level.Difficulty(surface,muteMusicButton,themeMgr)
            if level.difficulty != "":
                level.lvlSelect(surface,muteMusicButton,themeMgr)

        elif page == "Tutorial":
            page = tutorial.tutScreen(surface,muteMusicButton,themeMgr)


        elif page == "Pause":
            page = pause.pauseScreen(surface,muteMusicButton,themeToggle,themeMgr)
            themeToggle.draw(surface,themeMgr) # Theme Toggle Button

        elif page == "Board":
            # All the code to display things on the screen goes here
            clearButton.draw(surface,themeMgr) # clear button
            checkPuzzleButton.draw(surface,themeMgr) # check puzzle button
            muteMusicButton.draw(surface,themeMgr) # mute button
            timer.displayTime(surface, themeMgr) # show timer
            pauseB.draw(surface,themeMgr) # Pause button

            #FIXME - comments from Pedro on gameState
            if gameState == 0:
                board.displayBoard(surface,themeMgr) # grid and numbers
                board.displayBoxes(surface, themeMgr) # boxes in the grid
            elif gameState == 1:
                if solCorrect:
                    puzzleComplete.draw(surface,themeMgr)
                    pcMainMenu.draw(surface,themeMgr)
                else:
                    puzzleIncorrect.draw(surface,themeMgr)
                    tryAgain.draw(surface,themeMgr)
                    showSolution.draw(surface,themeMgr)

            if blinkSoln:
                blinkSoln = blink_anim.blink_anim(timer, board, surface, themeMgr, startTime) # very slow blinking animation to show solution briefly

        if level.solnName != "" and notNew:
            page = "Board"
            notNew = False
            board.setUpPuzzle(int(level.difficulty), level.solnName)
            timer.resetTimer()
            timer.setRunning(True)

        pygame.display.update() # Update the display only one per loop (otherwise get flickering)

        if page == "Pause Main":
            page = "Main Menu"
            gameState = 0
            canEditGrid = True
            notNew = True
            level.difficulty = ""
            level.solnName = ""

        elif page == "Resume":
            timer.setRunning(True)
            page = "Board"

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit() # Prevents error message when quitting

            if e.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()

                if e.button == 1 and muteMusicButton.rect.collidepoint(x, y): # left click on mute music button
                    muteMusicButton.toggleMusic(themeMgr) # mute/unmute music

                elif e.button == 1 and page == "Main Menu" and quitGame.rect.collidepoint(x, y): # quit game button
                    pygame.quit()
                    exit() # Prevents error message when qutting

                elif e.button == 1 and page == "Main Menu" and startGame.rect.collidepoint(x, y): # start game button
                    page = "Difficulty Selection"

                elif e.button == 1 and page == "Main Menu" and themeToggle.rect.collidepoint(x, y): # theme toggle button
                    themeMgr.toggleDarkMode()

                elif e.button == 1 and page == "Main Menu" and tut.rect.collidepoint(x, y):
                    page = "Tutorial"

                elif e.button == 1 and page == "Board" and pauseB.rect.collidepoint(x,y):
                    timer.setRunning(False)
                    page = "Pause"

                elif page == "Board" and gameState == 0:
                    if e.button == 1 and clearButton.rect.collidepoint(x, y) and canEditGrid and (not blinkSoln): # left click on clear button
                        board.clearGrid() # clear grid
                        timer.resetTimer()

                    if e.button == 1 and checkPuzzleButton.rect.collidepoint(x, y) and canEditGrid and (not blinkSoln): # left click on check button
                        # Check if user completed puzzle successfully
                        # If they did or they choose to see solution, prevent them from editing the grid
                        canEditGrid, solCorrect = checkPuzzleButton.checkPuzzle(board)
                        #gameState switches to 1, so popup appears and prevents interaction with board
                        gameState = 1
                        if solCorrect:
                            timer.setRunning(False) # stop the timer
                            canEditGrid = False

                    if (e.button == 1 or e.button == 3) and canEditGrid and (not blinkSoln): # click on box in grid
                        board.clickBox(x,y,e.button)

                elif page == "Board" and gameState == 1:
                    if solCorrect == False:
                        if e.button == 1 and tryAgain.rect.collidepoint(x, y):
                            gameState = 0

                        if e.button == 1 and showSolution.rect.collidepoint(x, y):
                            board.showSolution()
                            startTime = pygame.time.get_ticks() #keep track of time for blink animation
                            blinkSoln = True
                            gameState = 0

                    # Return to main menu
                    if solCorrect == True and e.button == 1 and pcMainMenu.rect.collidepoint(x, y) and canEditGrid == False:
                        page = "Main Menu"
                        gameState = 0
                        canEditGrid = True
                        notNew = True
                        level.difficulty = ""
                        level.solnName = ""

# Run in command prompt (otherwise closes instantly)
main()
