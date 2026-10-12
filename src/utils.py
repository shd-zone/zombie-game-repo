import os
import pygame

# Base directory setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)


def load_image(relative_path, scale=None):
    full_path = os.path.join(ROOT_DIR, relative_path)

    try:
        image = pygame.image.load(full_path).convert_alpha()

        if scale:
            image = pygame.transform.scale(image, scale)

        return image

    except (pygame.error, FileNotFoundError):
        print(f"[WARNING] Image not found: {full_path}")

        # Placeholder image
        placeholder = pygame.Surface((32, 32), pygame.SRCALPHA)
        placeholder.fill((255, 0, 0))

        return placeholder


def load_sound(relative_path):
    full_path = os.path.join(ROOT_DIR, relative_path)

    try:
        return pygame.mixer.Sound(full_path)

    except (pygame.error, FileNotFoundError):
        print(f"[WARNING] Sound not found: {full_path}")
        return None
    