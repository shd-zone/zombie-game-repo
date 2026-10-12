import random
from settings import *
from zombie import Zombie

class WaveManager:
    def __init__(self, game):
        self.game = game
        self.wave_number = 0
        self.zombies_to_spawn = 0
        self.spawn_timer = 0

    def start_new_wave(self):
        self.wave_number += 1
        self.zombies_to_spawn = self.wave_number * 4

    def update(self):
        if len(self.game.zombies) == 0 and self.zombies_to_spawn <= 0:
            self.start_new_wave()
            
        if self.zombies_to_spawn > 0:
            now = pygame.time.get_ticks()
            if now - self.spawn_timer > 1000:
                self.spawn_timer = now
                self.spawn_zombie()
                self.zombies_to_spawn -= 1

    def spawn_zombie(self):
        side = random.choice(['top', 'bottom', 'left', 'right'])
        if side == 'top': x, y = random.randint(0, WIDTH), -20
        elif side == 'bottom': x, y = random.randint(0, WIDTH), HEIGHT + 20
        elif side == 'left': x, y = -20, random.randint(0, HEIGHT)
        else: x, y = WIDTH + 20, random.randint(0, HEIGHT)
        Zombie(self.game, x, y)