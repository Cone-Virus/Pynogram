import pygame

# Constants
SCREEN_SIZE = WIDTH, HEIGHT = 800, 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def main():
    pygame.init() #Start Pygame

    # Set up screen (size, caption)
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Pynogram")

    # Clock controls speed of screen updates
    clock = pygame.time.Clock()

    # Main game loop
    while True: # Loop until quit

        for event in pygame.event.get(): # Event handlers
            if event.type == pygame.QUIT: # Quit game
                return

        screen.fill(WHITE) # White background

        createGrid(15,screen) # Draw the main grid (empty)

        clock.tick(60) # Limit game to 60 FPS
        pygame.display.flip() # Update the screen


# Create an (N x N) grid, where N = dimension
def createGrid(dimension,screen):
    # Width/height of entire grid
    GRID_FULL_SIZE = 500
    # Size of each box in the grid
    BOX_SIZE = GRID_FULL_SIZE / dimension
    # Position of top-left corner of grid
    GRID_X_POS = 150
    GRID_Y_POS = 150

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


main() #Run game
pygame.quit() #Quit game
