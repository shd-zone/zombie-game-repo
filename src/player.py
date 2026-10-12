import pygame
from settings import *
from bullet import Bullet
from utils import load_image

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self._groups = game.all_sprites
        super().__init__(self._groups)
        self.game = game
        
        self.original_image = load_image("assets/images/player/player.png", (40, 40))
        if isinstance(self.original_image, pygame.Surface) and self.original_image.get_size() == (32, 32):
            self.original_image.fill(GREEN)
            
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2(0, 0)
        self.rot = 0
        self.health = PLAYER_HEALTH
        self.last_shot = 0

    def get_keys(self):
        self.vel = pygame.math.Vector2(0, 0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]: self.vel.y = -PLAYER_SPEED
        if keys[pygame.K_s] or keys[pygame.K_DOWN]: self.vel.y = PLAYER_SPEED
        if keys[pygame.K_a] or keys[pygame.K_LEFT]: self.vel.x = -PLAYER_SPEED
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]: self.vel.x = PLAYER_SPEED
            
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071

        if pygame.mouse.get_pressed()[0]:
            self.shoot()

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > GUN_COOLDOWN:
            self.last_shot = now
            if self.game.shoot_sound:
                self.game.shoot_sound.play()
                
            mouse_pos = pygame.mouse.get_pos()
            dir_vec = pygame.math.Vector2(mouse_pos) - self.pos
            if dir_vec.length_squared() > 0:
                dir_vec = dir_vec.normalize()
            else:
                dir_vec = pygame.math.Vector2(1, 0)
            Bullet(self.game, self.pos, dir_vec)

    def update(self):
        self.get_keys()
        mouse_pos = pygame.mouse.get_pos()
        self.rot = (pygame.math.Vector2(mouse_pos) - self.pos).angle_to((1, 0))
        
        self.image = pygame.transform.rotate(self.original_image, self.rot)
        self.rect = self.image.get_rect(center=self.rect.center)
        
        self.pos += self.vel * self.game.dt * 60
        self.rect.center = self.pos
        
        if self.rect.left < 0: self.rect.left = 0
        if self.rect.right > WIDTH: self.rect.right = WIDTH
        if self.rect.top < 0: self.rect.top = 0
        if self.rect.bottom > HEIGHT: self.rect.bottom = HEIGHT
        self.pos = pygame.math.Vector2(self.rect.center)