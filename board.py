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

# Used for testing the Board class
def main():
    board = Board(10,"test.txt")
    board.printSolution()

    board2 = Board(5, "test2.txt")
    board2.printSolution()

# Run in command prompt (otherwise closes instantly)
main()
