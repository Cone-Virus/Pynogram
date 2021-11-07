import Button
# Button for clearing the board
class ClearButton(Button.Button):
    # Constructor
    def __init__(self, x, y, image):
        super(ClearButton, self).__init__(x, y, image)
