import pygame
import sys
from settings import *
from player import Player
from zombie import Zombie
from wave import WaveManager
from ui import UI
from utils import load_sound


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()

        self.shoot_sound = load_sound("sounds/shoot.wav")

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.zombies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        self.player = Player(self, WIDTH // 2, HEIGHT // 2)

        self.wave_manager = WaveManager(self)
        self.ui = UI(self)

        # Score
        self.score = 0

    def run(self):
        self.playing = True

        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000

            self.events()
            self.update()
            self.draw()

        self.show_game_over_screen()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        self.all_sprites.update()
        self.wave_manager.update()

        # Bullet hits Zombie
        hits = pygame.sprite.groupcollide(
            self.zombies,
            self.bullets,
            False,
            True
        )

        for zombie, bullets in hits.items():
            zombie.health -= BULLET_DAMAGE * len(bullets)

            if zombie.health <= 0:
                zombie.kill()
                self.score += 10

    def draw(self):
        self.screen.fill(BG_COLOR)

        self.all_sprites.draw(self.screen)

        self.ui.draw(self.screen)

        pygame.display.flip()

    def show_game_over_screen(self):
        waiting = True

        while waiting:

            self.ui.show_game_over(self.screen)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                    if event.key == pygame.K_r:
                        waiting = False
                        self.new()
                        self.run()