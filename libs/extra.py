import os

import pygame

assets_dir = "./assets"

# Yoinked from the docs: https://www.pygame.org/docs/tut/ChimpLineByLine.html
def load_image(name, colorkey=None, scale=1):
    fullname = os.path.join(assets_dir, name)
    image = pygame.image.load(fullname)

    size = image.get_size()
    size = (size[0] * scale, size[1] * scale)
    image = pygame.transform.scale(image, size)

    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    return image, image.get_rect()

def load_sound(name):
    class NoneSound:
        def play(self):
            pass

    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()

    fullname = os.path.join(assets_dir, name)
    sound = pygame.mixer.Sound(fullname)

    return sound