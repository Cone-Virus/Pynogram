import os
import pygame
import get_path

# Load an image from a file; imageName looks like "name.ext"
def load_image(imageName):
    imageName = "assets/" + imageName
    loadName = get_path.get_path(imageName)
    try:
        # Actually load the image here
        image = pygame.image.load(loadName).convert_alpha()
    except pygame.error as message:
        print("Unable to load the image ", imageName)
        raise SystemExit(message)
    return image, image.get_rect()
