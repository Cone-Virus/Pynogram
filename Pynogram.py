import os
import pygame
import math

# Get the directory of the assets
main_dir = os.path.split(os.path.abspath(__file__))[0]
assets_dir = os.path.join(main_dir, "assets")

class Board:

    # Array fill: 0 is blank, 1 is filled, 2 is 'X'
    solution = [] # Solution of the puzzle
    grid = []     # Game board
    size = 0      # Size of the puzzle - a (size x size) grid
    solNumsX = [] # Numbers to go along the left side of the grid
    solNumsY = [] # Numbers to go above the grid

    boardsize = 0 # Size of board on the screen

    # Initialize board (variables initialized in setUpPuzzle to prevent
    # needing a new board instance for each level)
    def __init__(self):
        self.solution = []
        self.grid = []
        self.solNumsX = []
        self.solNumsY = []

    # Set up puzzle with size, grid and solution arrays, numbers to go alongside grid
    def setUpPuzzle(self, size, filename):
        self.solution = []
        self.grid = []
        self.size = size
        for i in range(self.size): # Initialize both arrays
            self.grid.append([0]*self.size)
            self.solution.append([0]*self.size)
        self.loadSolution(filename) # Fill in the values for solution array

        #Set up row and column numbers
        self.solNumsX = self.solnRowNumbers()
        self.solNumsY = self.solnColNumbers()


    # Loads solution from text file
    def loadSolution(self,filename):
        filename = os.path.join(assets_dir, filename) # File is in assets folder
        rowCount = 0
        f = open(filename, 'r')
        for line in f.readlines(): # Each row
            colCount = 0
            for num in line.split(): # Each column
                self.solution[rowCount][colCount] = int(num) # Copy the value into array
                colCount = colCount + 1
            rowCount = rowCount + 1

    # Prints solution array
    def printSolution(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.solution[i][j], end="")
            print("\n")

    # Prints grid array
    def printGrid(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.grid[i][j], end="")
            print("\n")

    # Check if grid matches solution
    # Not a match if grid is filled (1) and solution is not filled (0 or 2)
    # Not a match if grid is not filled (0 or 2) and solution is filled (1)
    def checkSolution(self):
        for i in range(self.size):
            for j in range(self.size):
                if ( # Boxes are checked here
                    (self.grid[i][j] == 1) and (self.solution[i][j] != 1) or
                    (self.grid[i][j] != 1) and (self.solution[i][j] == 1)
                ):
                    return False
        return True # All boxes are correct


    # Show solution - set all boxes in grid to match solution
    def showSolution(self):
        for i in range(self.size):
            for j in range(self.size):
                self.grid[i][j] = self.solution[i][j]

    # Clears the grid (set all boxes to 0)
    def clearGrid(self):
        for i in range(self.size):
            for j in range(self.size):
                self.grid[i][j] = 0

    # Toggle fill of selected grid box
    def toggleFill(self, rowNum, colNum): # Row and column numbers start at 0
        if (self.grid[rowNum][colNum] == 1): # If already filled, set to blank
            self.grid[rowNum][colNum] = 0
        else: # Not filled, set to filled
            self.grid[rowNum][colNum] = 1

    # Toggle "X" of selected grid box
    def toggleX(self, rowNum, colNum): # Row and column numbers start at 0
        if (self.grid[rowNum][colNum] == 2): # If already "X", set to blank
            self.grid[rowNum][colNum] = 0
        else: # Not "X"", set to "X""
            self.grid[rowNum][colNum] = 2

    # Return the state (0, 1, or 2) of the grid box at the specified row and column
    def getGridBoxState(self, rowNum, colNum): # Row and column numbers start at 0
        return self.grid[rowNum][colNum]

    # Returns a list of the sizes of the "blocks" of the provided solution row
    # These numbers would be to the left of the corresponding row in the grid GUI
    def solnRowNumbers(self):
        fullList = [] # List to return

        for i in range(self.size): # each row
            currRowList = [] # Stores list for current row
            blockSize = 0    # Size of the block - determines what number appended to list
            isBlock = False  # Size of blank spaces doesn't go in list - this keeps track of when to append

            for j in range(self.size): # iterate through row
                if (self.solution[i][j] == 1): # part of block
                    isBlock = True
                    blockSize = blockSize + 1
                elif (isBlock): # space after a block - blockSize is now the size of the full block
                    currRowList.append(blockSize)
                    blockSize = 0
                    isBlock = False

            if (blockSize != 0): # no spaces after the final block - append its size
                currRowList.append(blockSize)
            if (not currRowList): # if list empty, append 0 (no blocks)
                currRowList.append(0)
            fullList.append(currRowList)
        return fullList

    # Returns a list of the sizes of the "blocks" of the provided solution row
    # These numbers would be to the left of the corresponding row in the grid GUI
    def solnColNumbers(self):
        fullList = [] # List to return

        for i in range(self.size): # each column
            currColList = [] # Stores list for current column
            blockSize = 0    # Size of the block - determines what number appended to list
            isBlock = False  # Size of blank spaces doesn't go in list - this keeps track of when to append

            for j in range(self.size): # iterate through column
                if (self.solution[j][i] == 1): # part of block
                    isBlock = True
                    blockSize = blockSize + 1
                elif (isBlock): # space after a block - blockSize is now the size of the full block
                    currColList.append(blockSize)
                    blockSize = 0
                    isBlock = False

            if (blockSize != 0): # no spaces after the final block - append its size
                currColList.append(blockSize)
            if (not currColList): # if list empty, append 0 (no blocks)
                currColList.append(0)
            fullList.append(currColList)
        return fullList

#-------------------------------------------------
# Start of code for interacting with display/user
#-------------------------------------------------
    def displayBoard(self, surface):
        self.color = (255,255,255)
        self.load_board(surface)
        if self.size == 5:
            self.boardsize = 180
        elif self.size == 10:
            self.boardsize = 355
        elif self.size == 15:
            self.boardsize = 530
        pygame.draw.rect(surface, (0,0,0), pygame.Rect(200, 250, self.boardsize, self.boardsize))
        for x in range(self.size):
            for y in range(self.size):
                self.button(x,y,surface)

    def button(self,x,y,surface):
        pygame.draw.rect(surface, self.color, pygame.Rect(205 + (x * 35), 255 + (y * 35), 30, 30))

    def load_board(self, surface):
        posX = 0 # Left Side
        for x in self.solNumsX:
            count = 0 # For numbers side to side
            x = reversed(x)
            for y in x:
                # Render numbers >= 10 in smaller font and fix spacing
                if y >= 10:
                    font = pygame.font.Font(None, 26)
                    text = font.render(str(y), True, (0,0,0))
                    surface.blit(text,(165 - (count * 35) ,260 + (posX * 35)))
                else:
                    font = pygame.font.Font(None, 30)
                    text = font.render(str(y), True, (0,0,0))
                    surface.blit(text,(175 - (count * 35) ,255 + (posX * 35)))

                count = count + 1
            posX = posX + 1
        posX = 0 # Top Side
        for x in self.solNumsY:
            count = 0 # For numbers top to bottom
            x = reversed(x)
            for y in x:

                # Render numbers >= 10 in smaller font and fix spacing
                if y >= 10:
                    font = pygame.font.Font(None, 26)
                    text = font.render(str(y), True, (0,0,0))
                    surface.blit(text,(205 + (posX * 35),(225  - (count * 35))))
                else:
                    font = pygame.font.Font(None, 30)
                    text = font.render(str(y), True, (0,0,0))
                    surface.blit(text,(210 + (posX * 35),(220  - (count * 35))))

                count = count + 1
            posX = posX + 1

    # Display each of the boxes, with displayed color depending on their state
    # 0 - blank - white; 1 - filled - black/grey; 2 - X - red
    def displayBoxes(self, surface):
        for i in range(self.size): # each row
            for j in range(self.size): # each column

                # Define upper left corner of grid square, used for positioning
                upperLeftX = 205 + (j * 35)
                upperLeftY = 255 + (i * 35)

                if self.grid[i][j] == 0: # blank
                    pygame.draw.rect(surface, (255,255,255), pygame.Rect(upperLeftX, upperLeftY, 30, 30))

                elif self.grid[i][j] == 1: # filled
                    # White background
                    pygame.draw.rect(surface, (255,255,255), pygame.Rect(upperLeftX, upperLeftY, 30, 30))
                    # Black square for the fill
                    pygame.draw.rect(surface, (0,0,0), pygame.Rect(upperLeftX + 3, upperLeftY + 3, 24, 24))

                else: # self.grid[i][j] == 2, X
                    # White background
                    pygame.draw.rect(surface, (255,255,255), pygame.Rect(upperLeftX, upperLeftY, 30, 30))
                    # Two red lines to make the X:
                    pygame.draw.line(surface, (255,0,0), (upperLeftX + 5, upperLeftY + 3), (upperLeftX + 23, upperLeftY + 26), 6)
                    pygame.draw.line(surface, (255,0,0), (upperLeftX + 23, upperLeftY + 3), (upperLeftX + 5, upperLeftY + 26), 6)


    def convert_space(self,x,y): # Function responsible for converting X,Y mouse coordinates into array numbers
        new_x = math.floor((x - 205) / 35)
        new_y = math.floor((y - 255) / 35)
        if new_x < 0:
            new_x = 0
        if new_y < 0:
            new_y = 0
        if new_x >= self.size:
            new_x = self.size - 1
        if new_y >= self.size:
            new_y = self.size - 1
        return new_x, new_y

    # Handles changes in box states when clicked on
    def clickBox(self,x,y,selection):
        if x <= self.boardsize + 205 and y <= self.boardsize + 255 and x >= 200 and y >= 250:
            col,row = self.convert_space(x,y) # Get the row and column of the box to toggle
            if selection == 1: # left click - toggle fill
                self.toggleFill(row,col)
            elif selection == 3: # right click - toggle X
                self.toggleX(row,col)


# Load an image from a file; imageName looks like "name.ext"
def load_image(imageName):
    # Need image name to include path to load it into game
    loadName = os.path.join(assets_dir, imageName)
    try:
        # Actually load the image here
        image = pygame.image.load(loadName).convert_alpha()
    except pygame.error as message:
        print("Unable to load the image ", imageName)
        raise SystemExit(message)
    return image, image.get_rect()


#Popup buttons
class button():
    def __init__(self,x,y,image):
        self.image, self.rect = load_image(image)
        self.rect.topleft = (x,y)
    def draw(self,surface):
        #draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

#-------------------------------------------------
# End of code for interacting with display/user
#-------------------------------------------------

# Button for clearing the board
class ClearButton(pygame.sprite.Sprite):
    # Constructor
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("clear.bmp")
        self.rect.topleft = 725, 60 # Position on screen

# Button for checking the puzzle
class CheckPuzzleButton(pygame.sprite.Sprite):
    # Constructor
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("check.bmp")
        self.rect.topleft = 350, 700 # Position on screen

    # Determine if user completed the puzzle, and display appropriate message
    # YES: congratulation message, NO: give options to keep trying or show solution
    # If user has completed puzzle or chooses to show solution, return value indicating they
    # can no longer edit the puzzle/grid
    # FIXME - needs popups and buttons, not console text
    def checkPuzzle(self, board):
        isCorrect = board.checkSolution() # Check if user's solution is correct
        # FIXME - need to add the popups
        if isCorrect:
            solCorrect = True
            canEditGrid = False
        else:
            solCorrect = False
            canEditGrid = True

        return canEditGrid, solCorrect

# Button for muting/unmuting the music
class MuteMusicButton(pygame.sprite.Sprite):
    # Keeps track of whether music is on or not
    musicEnabled = True

    # Constructor
    def __init__(self):
        self.musicEnabled = True
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("music-on.bmp")
        self.rect.topleft = 790, 800 # Position on screen

    # Change sprite and toggle music based on current state
    def toggleMusic(self):
        if self.musicEnabled: # music on -> mute music
            self.musicEnabled = False
            pygame.mixer.music.pause()
            self.image, self.rect = load_image("music-off.bmp")
            self.rect.topleft = 790, 800 # Position on screen
        else: # music off -> turn on music
            self.musicEnabled = True
            pygame.mixer.music.unpause()
            self.image, self.rect = load_image("music-on.bmp")
            self.rect.topleft = 790, 800 # Position on screen

class Timer():
    timerRunning = True # counts up when true, stops when False
    refTime = 0 # time when timer started
    currTime = 0 # time relative to when timer started; what to display on the screen
    timerText = "" # text to show timer on screen

    # Used to display the time on screen
    numSeconds = 0
    numMinutes = 0

    def __init__(self):
        self.timerRunning = True
        self.refTime = pygame.time.get_ticks()
        self.currTime = pygame.time.get_ticks() - self.refTime # get the relative time
        self.numSeconds = 0
        self.numMinutes = 0
        self.timerText = ""

    def isRunning(self): # true if timer running, false otherwise (getter)
        return self.timerRunning

    def setRunning(self, status): # set timerRunning to status (setter)
        self.timerRunning = status

    def resetTimer(self): # start counting from 0
        self.refTime = pygame.time.get_ticks() # updates the reference time (new starting point)

    def displayTime(self, surface): # display the time on the screen
        # Only update time if timer is running
        if self.timerRunning:
            # Determine amount of time passed since refTime was set up
            self.currTime = pygame.time.get_ticks() - self.refTime
        self.numSeconds = self.currTime // 1000 # ms -> s
        self.numMinutes = self.numSeconds // 60 # s -> min
        self.numSeconds = self.numSeconds - (self.numMinutes * 60) # remove the time accounted for in numMinutes

        # Black box for border around timer
        pygame.draw.rect(surface, (0,0,0), pygame.Rect(395, 45, 110, 55))
        # White background for timer
        pygame.draw.rect(surface, (255,255,255), pygame.Rect(400, 50, 100, 45))

        # Display timer text (minutes and seconds)
        self.timerText = "{0:02}:{1:02}".format(self.numMinutes, self.numSeconds)
        font = pygame.font.Font(None, 30)
        text = font.render(self.timerText, True, (0,0,0))
        surface.blit(text, [408, 60])


def main():

    clock = pygame.time.Clock()
    screen = pygame.init()
    surface = pygame.display.set_mode((900,900))
    pygame.display.set_caption("Pynogram")
    surface.fill((255,255,255))

    timer = Timer()

    # Determines whether user can edit grid (including clear grid)
    # Check solution is also disabled; since user can't modify grid, result of check won't change
    # This is false when:
    # (1) User has checked their solution and is correct (completed the puzzle)
    # (2) User has checked their solution and is wrong, but chooses to see solution
    # (3) User is not on the board (ex. popup is covering it, different menu)
    canEditGrid = True
    solCorrect = False
    #Used when puzzle incorrect, prevents game from continuing until user selects to try again or give up

    # Set up clear button, check button, mute music button (sprites)
    clearButton = ClearButton()
    checkPuzzleButton = CheckPuzzleButton()
    muteMusicButton = MuteMusicButton()
    sprites = pygame.sprite.RenderPlain((clearButton,checkPuzzleButton, muteMusicButton))

    #Popup buttons
    puzzleComplete = button(50,115, "puzzleComplete.png")
    pcMainMenu = button(325,495, "mainmenu.png")
    puzzleIncorrect = button(50,115, "incorrect.png")
    tryAgain = button(325,420, "tryAgain.png")
    showSolution = button(325, 510, "showSolution.png")

    # Create a 10x10 board with solution from file "10-1.txt" (in assets folder)
    board = Board()
    board.setUpPuzzle(10, "10-1.txt")

    # Display the board lines and numbers
    board.displayBoard(surface)

    # Load song
    pygame.mixer.music.load(os.path.join(assets_dir, "Arpent.mp3"))
    pygame.mixer.music.play(-1) # loop indefinitely

    #Used to prevent interaction with puzzle while popup is active
    gameState = 0

    while True:
        clock.tick(60) # 60 fps

        # All the code to display things on the screen goes here
        surface.fill((255,255,255)) # white background
        sprites.draw(surface) # clear, check, mute buttons
        timer.displayTime(surface) # show timer

        #FIXME - comments from Pedro on gameState
        #gameState controls what is being rendered on screen, as well as what buttons are clickable
        #The default is 0, and allows access to the pynogram puzzle, clear button, and check solution button
        #gameState = 1 stops rendering the pynogram puzzle, and the buttons become unclickable.
        #State 1 renders a popup based on whether solCorrect is true or false
        #When solCorrect is false, user can click "Try Again" or "Show Solution" buttons, when solCorrect is true there is no functionality atm
        if gameState == 0:
            board.displayBoard(surface) # grid and numbers
            board.displayBoxes(surface) # boxes in the grid
        elif gameState == 1:
            if solCorrect:
                puzzleComplete.draw(surface)
                pcMainMenu.draw(surface)
            else:
                puzzleIncorrect.draw(surface)
                tryAgain.draw(surface)
                showSolution.draw(surface)

        pygame.display.update() # Update the display only one per loop (otherwise get flickering)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()

                if e.button == 1 and muteMusicButton.rect.collidepoint(x, y): # left click on mute music button
                    muteMusicButton.toggleMusic() # mute/unmute music

                if gameState == 0:
                    if e.button == 1 and clearButton.rect.collidepoint(x, y) and canEditGrid: # left click on clear button
                        board.clearGrid() # clear grid
                        timer.resetTimer()

                    if e.button == 1 and checkPuzzleButton.rect.collidepoint(x, y) and canEditGrid: # left click on check button
                        # Check if user completed puzzle successfully
                        # If they did or they choose to see solution, prevent them from editing the grid
                        canEditGrid, solCorrect = checkPuzzleButton.checkPuzzle(board)
                        #gameState switches to 1, so popup appears and prevents interaction with board
                        gameState = 1

                    if (e.button == 1 or e.button == 3) and canEditGrid: # click on box in grid
                        selection = e.button
                        board.clickBox(x,y,selection)

                if gameState == 1:
                    if solCorrect == False:
                        if e.button == 1 and tryAgain.rect.collidepoint(x, y):
                            #!!surface.fill((255, 255, 255))
                            #!!board.displayBoard(surface)
                            gameState = 0

                        if e.button == 1 and showSolution.rect.collidepoint(x, y):
                            timer.setRunning(False) # stop the timer
                            canEditGrid = False
                            board.showSolution()
                            gameState = 0

                    if solCorrect == True:
                        timer.setRunning(False) # stop the timer
                        canEditGrid = False

                        # Functionality to return to main menu - not currently enabled
                        #if e.button == 1 and pcMainMenu.rect.collidepoint(x, y) and canEditGrid == False:


# Run in command prompt (otherwise closes instantly)
main()
