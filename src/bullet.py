import pygame
from settings import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, pos, direction):
        self._groups = game.all_sprites, game.bullets
        super().__init__(self._groups)
        self.game = game
        
        self.image = pygame.Surface((8, 8))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.pos = pygame.math.Vector2(pos)
        self.rect.center = self.pos
        
        self.vel = direction * BULLET_SPEED

    def update(self):
        self.pos += self.vel * self.game.dt * 60
        self.rect.center = self.pos
        
        if not pygame.Rect(0, 0, WIDTH, HEIGHT).contains(self.rect):
            self.kill()