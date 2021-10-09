import os

# Get the directory of the assets
main_dir = os.path.split(os.path.abspath(__file__))[0]
assets_dir = os.path.join(main_dir, "assets")

class Board:

    # Array fill: 0 is blank, 1 is filled, 2 is 'X'
    solution = [] # Solution of the puzzle
    grid = []     # Game board
    size = 0      # Size of the puzzle - a (size x size) grid

    # Set size of puzzle, set up grid and solution arrays
    def __init__(self, size, filename):
        self.solution = []
        self.grid = []
        self.size = size
        for i in range(self.size): # Initialize both arrays
            self.grid.append([0]*self.size)
            self.solution.append([0]*self.size)
        self.loadSolution(filename) # Fill in the values for solution array

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
    def solnRowNumbers(self, rowNum): # Row numbers start at 0
        numRowList = []    # List to return
        blockSize = 0      # Size of the block - determines what number appended to list
        isBlock = False    # Size of blank spaces doesn't go in list - this keeps track of when to append

        for j in range(self.size): # iterate through row
            if (self.solution[rowNum][j] == 1): # part of block
                isBlock = True
                blockSize = blockSize + 1
            elif (isBlock): # space after a block - blockSize is now the size of the full block
                numRowList.append(blockSize)
                blockSize = 0
                isBlock = False
        if (blockSize != 0): # no spaces after the final block - append its size
                numRowList.append(blockSize)
        if (not numRowList): # if list empty, append 0 (no blocks)
            numRowList.append(0)
        return numRowList # return the list

    # Returns a list of the sizes of the "blocks" of the provided solution column
    # These numbers would be above the corresponding column in the grid GUI
    def solnColNumbers(self, colNum): # Column numbers start at 0
        numColList = []    # List to return
        blockSize = 0      # Size of the block - determines what number appended to list
        isBlock = False    # Size of blank spaces doesn't go in list - this keeps track of when to append

        for i in range(self.size): # iterate through row
            if (self.solution[i][colNum] == 1): # part of block
                isBlock = True
                blockSize = blockSize + 1
            elif (isBlock): # space after a block - blockSize is now the size of the full block
                numColList.append(blockSize)
                blockSize = 0
                isBlock = False
        if (blockSize != 0): # no spaces after the final block - append its size
                numColList.append(blockSize)
        if (not numColList): # if list empty, append 0 (no blocks)
            numColList.append(0)
        return numColList # return the list


# Used for testing the Board class, currently has demo of main functionality
def main():

    # Create a 5x5 board with solution from file "test3.txt" (in assets folder)
    board = Board(5,"test3.txt")

    # Print the solution and the grid
    print("Solution:")
    board.printSolution()
    print("Grid:")
    board.printGrid()

    # Change some grid values and display the grid again
    # 0 = blank, 1 = filled, 2 = X
    # Row and column numbers start at 0; a value of 5 is out of range for this
    board.toggleFill(0,0)
    board.toggleX(4,4)
    print("After changes, grid is:")
    board.printGrid()

    # Print the values of some grid boxes using getGridBoxState()
    # Row and column numbers start at 0; a value of 5 is out of range for this
    print("State of box at row 0, column 0 is: ", board.getGridBoxState(0,0)) # upper left, 1
    print("State of box at row 4, column 4 is: ", board.getGridBoxState(4,4)) # bottom right, 2
    print("State of box at row 2, column 2 is: ", board.getGridBoxState(2,2)) # center, 0

    # Clear the grid, display it again
    board.clearGrid()
    print("\nAfter clearing, grid is:")
    board.printGrid()

    # The grid for this board doesn't match the solution, so checkSolution() returns False
    print("Result of checkSolution for board is", board.checkSolution())

    # Load in a board with the solution all 0 (blank) to match the default grid, which is all 0 (blank)
    # Since the grid and solution match, checkSolution() returns True
    boardSolnBlank = Board(5, "test2.txt")
    print("Result of checkSolution for boardSolnBlank is", boardSolnBlank.checkSolution())

    # Print a list of numbers to go next to each row/column of the grid in the GUI
    # The numbers represent the sizes of the "blocks" in each row/column of the solution
    # In the GUI, numbers go to the left of each row and above each column
    # For a better idea of how this will look, look at images for "picross"
    # Row and column numbers start at 0; a value of 5 is out of range for this
    print("\nSolution is:")
    board.printSolution()
    print("Numbers for row 0:", board.solnRowNumbers(0))
    print("Numbers for row 1:", board.solnRowNumbers(1))
    print("Numbers for row 2:", board.solnRowNumbers(2))
    print("Numbers for row 3:", board.solnRowNumbers(3))
    print("Numbers for row 4:", board.solnRowNumbers(4))
    print("")
    print("Numbers for column 0:", board.solnColNumbers(0))
    print("Numbers for column 1:", board.solnColNumbers(1))
    print("Numbers for column 2:", board.solnColNumbers(2))
    print("Numbers for column 3:", board.solnColNumbers(3))
    print("Numbers for column 4:", board.solnColNumbers(4))


# Run in command prompt (otherwise closes instantly)
main()
