import pygame
from settings import *
from utils import load_image


class Zombie(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self._groups = game.all_sprites, game.zombies
        super().__init__(self._groups)

        self.game = game

        # Zombie sprite
        self.original_image = load_image(
            "assets/zombies/Enemies/Tiles/tile_0000.png",
            (40, 40)
        )

        # Placeholder check
        if self.original_image.get_size() == (32, 32):
            self.original_image.fill(RED)

        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2(0, 0)
        self.health = ZOMBIE_HEALTH

    def update(self):
        if not self.game.player:
            return

        # Move towards player
        direction = self.game.player.pos - self.pos

        if direction.length_squared() > 0:
            direction = direction.normalize()

        self.vel = direction * ZOMBIE_SPEED
        self.pos += self.vel * self.game.dt * 60
        self.rect.center = self.pos

        # Damage player on collision
        if self.rect.colliderect(self.game.player.rect):
            self.game.player.health -= ZOMBIE_DAMAGE * self.game.dt

            if self.game.player.health <= 0:
                self.game.playing = False