import os
import pygame
from settings import ROOT_DIR


def resource_path(relative_path):
    """
    Returns absolute path for assets/resources.
    Works on Windows and Browser (Pygbag).
    """
    return os.path.join(ROOT_DIR, relative_path)


def load_image(path, size=None):
    full_path = resource_path(path)

    try:
        image = pygame.image.load(full_path).convert_alpha()

        if size:
            image = pygame.transform.scale(image, size)

        return image

    except Exception as e:
        print(f"[IMAGE ERROR] {full_path}")
        print(e)

        # Fallback image
        fallback_size = size if size else (32, 32)
        image = pygame.Surface(fallback_size, pygame.SRCALPHA)
        image.fill((255, 0, 255))  # Pink = Missing Texture

        return image


def load_sound(path):
    full_path = resource_path(path)

    try:
        return pygame.mixer.Sound(full_path)

    except Exception as e:
        print(f"[SOUND WARNING] {full_path}")
        print(e)

        return None