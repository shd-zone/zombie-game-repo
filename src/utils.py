import pygame

def load_image(path, scale=None):
    try:
        img = pygame.image.load(path).convert_alpha()
        if scale:
            img = pygame.transform.scale(img, scale)
        return img
    except pygame.error:
        # Fallback agar image file missing ho
        surface = pygame.Surface((32, 32))
        surface.fill((200, 50, 50))
        return surface

def load_sound(path):
    try:
        return pygame.mixer.Sound(path)
    except pygame.error:
        return None