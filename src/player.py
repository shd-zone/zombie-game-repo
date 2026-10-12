import pygame
from settings import *
from bullet import Bullet
from utils import load_image

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self._groups = game.all_sprites
        super().__init__(self._groups)
        self.game = game

        # Load full spritesheet
        sheet = load_image("assets/player/Spritesheet/roguelikeChar_transparent.png")

        # First character (top-left)
        sprite = pygame.Surface((16, 16), pygame.SRCALPHA)
        sprite.blit(sheet, (0, 0), (0, 0, 16, 16))

        # Scale for game
        self.original_image = pygame.transform.scale(sprite, (48, 48))

        self.image = self.original_image
        self.rect = self.image.get_rect(center=(x, y))

        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2()
        self.rot = 0
        self.health = PLAYER_HEALTH
        self.last_shot = 0

    def get_keys(self):
        self.vel = pygame.math.Vector2()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.vel.y = -PLAYER_SPEED
        if keys[pygame.K_s]:
            self.vel.y = PLAYER_SPEED
        if keys[pygame.K_a]:
            self.vel.x = -PLAYER_SPEED
        if keys[pygame.K_d]:
            self.vel.x = PLAYER_SPEED

        if self.vel.length_squared() > 0:
            self.vel = self.vel.normalize() * PLAYER_SPEED

        if pygame.mouse.get_pressed()[0]:
            self.shoot()

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > GUN_COOLDOWN:
            self.last_shot = now

            if self.game.shoot_sound:
                self.game.shoot_sound.play()

            mouse = pygame.math.Vector2(pygame.mouse.get_pos())
            direction = mouse - self.pos

            if direction.length_squared() > 0:
                direction = direction.normalize()

            Bullet(self.game, self.pos, direction)

    def update(self):
        self.get_keys()

        mouse = pygame.math.Vector2(pygame.mouse.get_pos())
        self.rot = (mouse - self.pos).angle_to((1, 0))

        self.image = pygame.transform.rotate(self.original_image, self.rot)
        self.rect = self.image.get_rect(center=self.rect.center)

        self.pos += self.vel * self.game.dt * 60
        self.rect.center = self.pos