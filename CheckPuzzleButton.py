import Button
# Button for checking the puzzle
class CheckPuzzleButton(Button.Button):
    # Constructor
    def __init__(self, x, y, image):
        super(CheckPuzzleButton, self).__init__(x, y, image)

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
