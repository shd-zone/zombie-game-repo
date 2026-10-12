import pygame
from settings import *
from utils import load_image

class Zombie(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self._groups = game.all_sprites, game.zombies
        super().__init__(self._groups)
        self.game = game
        
        self.image = load_image("assets/images/zombies/zombie.png", (35, 35))
        if isinstance(self.image, pygame.Surface) and self.image.get_size() == (32, 32):
            self.image.fill(RED)
            
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2(0, 0)
        self.health = ZOMBIE_HEALTH

    def update(self):
        if self.game.player:
            dir_vec = self.game.player.pos - self.pos
            if dir_vec.length_squared() > 0:
                dir_vec = dir_vec.normalize()
            self.vel = dir_vec * ZOMBIE_SPEED
            
            self.pos += self.vel * self.game.dt * 60
            self.rect.center = self.pos

            if self.rect.colliderect(self.game.player.rect):
                self.game.player.health -= ZOMBIE_DAMAGE * self.game.dt
                if self.game.player.health <= 0:
                    self.game.playing = False