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
        pygame.display.flip()

    def button(self,x,y,surface):
        pygame.draw.rect(surface, self.color, pygame.Rect(205 + (x * 35), 255 + (y * 35), 30, 30))

    def load_board(self, surface):
        posX = 0 # Left Side
        for x in self.solNumsX:
            count = 0 # For numbers side to side
            x = reversed(x)
            for y in x:
                font = pygame.font.Font('freesansbold.ttf', 30)
                text = font.render(str(y), True, (0,0,0))
                surface.blit(text,(175 - (count * 35) ,255 + (posX * 35)))
                count = count + 1
            posX = posX + 1
        posX = 0 # Top Side
        for x in self.solNumsY:
            count = 0 # For numbers top to bottom
            x = reversed(x)
            for y in x:
                font = pygame.font.Font('freesansbold.ttf', 30)
                text = font.render(str(y), True, (0,0,0))
                surface.blit(text,(210 + (posX * 35),(220  - (count * 35))))
                count = count + 1
            posX = posX + 1

    # Display each of the boxes, with displayed color depending on their state
    # 0 - blank - white; 1 - filled - black/grey; 2 - X - red
    def displayBoxes(self, surface):
        for i in range(self.size): # each row
            for j in range(self.size): # each column
                if self.grid[i][j] == 0: # blank
                    pygame.draw.rect(surface, (255,255,255), pygame.Rect(205 + (i * 35), 255 + (j * 35), 30, 30))
                elif self.grid[i][j] == 1: # filled
                    pygame.draw.rect(surface, (45,45,45), pygame.Rect(205 + (i * 35), 255 + (j * 35), 30, 30))
                else: # self.grid[i][j] == 2, X
                    pygame.draw.rect(surface, (90,45,90), pygame.Rect(205 + (i * 35), 255 + (j * 35), 30, 30))

        pygame.display.update()

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
            row,col = self.convert_space(x,y) # Get the row and column of the box to toggle

            if selection == 1: # left click - toggle fill
                self.toggleFill(row,col)
            elif selection == 3: # right click - toggle X
                self.toggleX(row,col)

#-------------------------------------------------
# End of code for interacting with display/user
#-------------------------------------------------

def main():

    clock = pygame.time.Clock()
    screen = pygame.init()
    surface = pygame.display.set_mode((900,900))
    surface.fill((255,255,255))

    # Create a 10x10 board with solution from file "test.txt" (in assets folder)
    board = Board()
    board.setUpPuzzle(5, "test4.txt")

    # Display the board lines and numbers
    board.displayBoard(surface)

    while True:
        clock.tick(60) # 60 fps

        # Display all the boxes, with color dependent on their current state
        board.displayBoxes(surface)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1 or e.button == 3:
                    x,y = pygame.mouse.get_pos()
                    selection = e.button
                    board.clickBox(x,y,selection)




# Run in command prompt (otherwise closes instantly)
main()
