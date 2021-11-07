import os
import pygame
import math
import get_path

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
        filename = "assets/" + filename
        filename = get_path.get_path(filename)
        rowCount = 0
        f = open(filename, 'r')
        for line in f.readlines(): # Each row
            colCount = 0
            for num in line.split(): # Each column
                self.solution[rowCount][colCount] = int(num) # Copy the value into array
                colCount = colCount + 1
            rowCount = rowCount + 1

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

    def displayBoard(self, surface): # General initialization of board
        self.color = (255,255,255)
        if self.size == 5:
            self.boardX = 350
            self.boardY = 350
            self.boardsize = 180
        elif self.size == 10:
            self.boardX = 275
            self.boardY = 275
            self.boardsize = 355
        elif self.size == 15:
            self.boardX = 185
            self.boardY = 240
            self.boardsize = 530
        self.load_board(surface)
        pygame.draw.rect(surface, (0,0,0), pygame.Rect(self.boardX, self.boardY, self.boardsize, self.boardsize))
        for x in range(self.size):
            for y in range(self.size):
                self.button(x,y,surface)

    def button(self,x,y,surface):
        pygame.draw.rect(surface, self.color, pygame.Rect(self.boardX + 5 + (x * 35), self.boardY + 5 + (y * 35), 30, 30))

    def load_board(self, surface):
        posX = 0 # Left Side
        for x in self.solNumsX:
            count = 0 # For numbers side to side
            x = reversed(x)
            for y in x:
                # Render numbers >= 10 in smaller font and fix spacing
                if y >= 10:
                    font = pygame.font.Font(get_path.get_path("assets/font/freesansbold.ttf"), 26)
                    text = font.render(str(y), True, (0,0,0))
                    surface.blit(text,(self.boardX - 40 - (count * 35) ,self.boardY + 10 + (posX * 35)))
                else:
                    font = pygame.font.Font(get_path.get_path("assets/font/freesansbold.ttf"), 30)
                    text = font.render(str(y), True, (0,0,0))
                    surface.blit(text,(self.boardX - 35 - (count * 35) ,self.boardY + 5 + (posX * 35)))

                count = count + 1
            posX = posX + 1
        posX = 0 # Top Side
        for x in self.solNumsY:
            count = 0 # For numbers top to bottom
            x = reversed(x)
            for y in x:
                # Render numbers >= 10 in smaller font and fix spacing
                if y >= 10:
                    font = pygame.font.Font(get_path.get_path("assets/font/freesansbold.ttf"), 26)
                    text = font.render(str(y), True, (0,0,0))
                    surface.blit(text,(self.boardX + 5 + (posX * 35),(self.boardY - 40 - (count * 35))))
                else:
                    font = pygame.font.Font(get_path.get_path("assets/font/freesansbold.ttf"), 30)
                    text = font.render(str(y), True, (0,0,0))
                    surface.blit(text,(self.boardX + 8 + (posX * 35),(self.boardY - 40 - (count * 35))))

                count = count + 1
            posX = posX + 1

    # Display each of the boxes, with displayed color depending on their state
    # 0 - blank - white; 1 - filled - black/grey; 2 - X - red
    def displayBoxes(self, surface):
        for i in range(self.size): # each row
            for j in range(self.size): # each column

                # Define upper left corner of grid square, used for positioning
                upperLeftX = self.boardX + 5 + (j * 35)
                upperLeftY = self.boardY + 5 + (i * 35)

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
        new_x = math.floor((x - self.boardX + 5) / 35)
        new_y = math.floor((y - self.boardY + 5) / 35)
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
        if x <= self.boardsize + self.boardX + 5 and y <= self.boardsize + self.boardY + 5 and x >= self.boardX and y >= self.boardY:
            col,row = self.convert_space(x,y) # Get the row and column of the box to toggle
            if selection == 1: # left click - toggle fill
                self.toggleFill(row,col)
            elif selection == 3: # right click - toggle X
                self.toggleX(row,col)
