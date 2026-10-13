import pygame
from settings import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, pos, direction):
        self._groups = game.all_sprites, game.bullets
        super().__init__(self._groups)

        self.game = game

        # Yellow Bullet
        self.image = pygame.Surface((8, 8), pygame.SRCALPHA)
        pygame.draw.circle(self.image, YELLOW, (4, 4), 4)

        self.rect = self.image.get_rect(center=pos)

        self.pos = pygame.math.Vector2(pos)
        self.vel = direction * BULLET_SPEED

    def update(self):
        self.pos += self.vel * self.game.dt * 60
        self.rect.center = self.pos

        if (
            self.rect.right < 0 or
            self.rect.left > WIDTH or
            self.rect.bottom < 0 or
            self.rect.top > HEIGHT
        ):
            self.kill()