import os
import pygame
from pygame.compat import geterror

# Constants
SCREEN_SIZE = WIDTH, HEIGHT = 900, 900
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Get the directory of the assets
main_dir = os.path.split(os.path.abspath(__file__))[0]
assets_dir = os.path.join(main_dir, "assets")

# Create an (N x N) grid, where dimension = N
def createGrid(dimension,screen):
    # Width/height of entire grid
    GRID_FULL_SIZE = 500
    # Size of each box in the grid
    BOX_SIZE = GRID_FULL_SIZE / dimension
    # Position of top-left corner of grid
    GRID_X_POS = 200
    GRID_Y_POS = 250

    #Thickness of grid lines
    lineWeight = 3

    # Draw the outer edges
    pygame.draw.line(screen, BLACK, (GRID_X_POS, GRID_Y_POS), (GRID_FULL_SIZE + GRID_X_POS, GRID_Y_POS), lineWeight)
    pygame.draw.line(screen, BLACK, (GRID_X_POS, GRID_FULL_SIZE + GRID_Y_POS), (GRID_FULL_SIZE + GRID_X_POS, GRID_FULL_SIZE + GRID_Y_POS), lineWeight)
    pygame.draw.line(screen, BLACK, (GRID_X_POS, GRID_Y_POS), (GRID_X_POS, GRID_FULL_SIZE + GRID_Y_POS), lineWeight)
    pygame.draw.line(screen, BLACK, (GRID_FULL_SIZE + GRID_X_POS, GRID_Y_POS), (GRID_FULL_SIZE + GRID_X_POS, GRID_FULL_SIZE + GRID_Y_POS), lineWeight)

    # Draw the lines between boxes
    for num in range(dimension):
        if ( (num % 5 == 0) and (num > 0) ): # Make interior lines bold - divide grid into (5 x 5) sections
            lineWeight = 5
        else:
            lineWeight = 3
        # Vertical lines
        pygame.draw.line(screen, BLACK, (GRID_X_POS + (BOX_SIZE * num), GRID_Y_POS), (GRID_X_POS + (BOX_SIZE * num), GRID_FULL_SIZE + GRID_Y_POS), lineWeight)
        # Horizontal lines
        pygame.draw.line(screen, BLACK, (GRID_X_POS, GRID_Y_POS + (BOX_SIZE * num)),(GRID_FULL_SIZE + GRID_X_POS, GRID_Y_POS + (BOX_SIZE * num)), lineWeight)

# Load an image from a file; imageName looks like "name.ext"
def load_image(imageName):
    # Need image name to include path to load it into game
    loadName = os.path.join(assets_dir, imageName)
    try:
        # Actually load the image here
        image = pygame.image.load(loadName).convert()
    except pygame.error as message:
        print("Unable to load the image ", name)
        raise SystemExit(message)
    return image, image.get_rect()

# Button for clearing the board, 
class ClearButton(pygame.sprite.Sprite):
    # Constructor
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("clear.bmp")
        self.rect.topleft = 725, 60 # Position on screen

    # Clear board, activates when clicked (condition in main loop)
    def clearBoard(self):
        print("(TEST) Clear Button clicked - need to implement clear function")
        #FIXME - add clearing board

def main():
    pygame.init() #Start Pygame

    # Set up screen (size, caption)
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Pynogram")

    # Clock controls speed of screen updates
    clock = pygame.time.Clock()

    #FIXME
    clearButton = ClearButton()
    sprites = pygame.sprite.RenderPlain((clearButton))
    #FIXME

    # Main game loop
    while True: # Loop until quit
        clock.tick(60) # Limit game to 60 FPS

        # Event handlers
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Quit game
                return
            elif event.type == pygame.MOUSEBUTTONDOWN: # Mouse click
                x, y = pygame.mouse.get_pos()
                # Clear button
                if clearButton.rect.collidepoint(x, y):
                    clearButton.clearBoard()

        screen.fill(WHITE)     # White background
        createGrid(15, screen) # Draw grid
        sprites.draw(screen)   # Draw sprites
        pygame.display.flip()  # Update the screen


main() # Run game
pygame.quit() # Quit game
