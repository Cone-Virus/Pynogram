import os
import pygame

# Load an image from a file; imageName looks like "name.ext"
def load_image(imageName):
    # Get the directory of the assets
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    assets_dir = os.path.join(main_dir, "assets")
    
    # Need image name to include path to load it into game
    loadName = os.path.join(assets_dir, imageName)
    try:
        # Actually load the image here
        image = pygame.image.load(loadName).convert_alpha()
    except pygame.error as message:
        print("Unable to load the image ", imageName)
        raise SystemExit(message)
    return image, image.get_rect()
