import pygame
from settings import *

class UI:
    def __init__(self, game):
        self.game = game
        try:
            self.font = pygame.font.Font(None, 36)
            self.big_font = pygame.font.Font(None, 64)
        except:
            self.font = pygame.font.SysFont("Arial", 36)
            self.big_font = pygame.font.SysFont("Arial", 64)

    def draw(self, surface):
        hp_text = self.font.render(f"Health: {int(max(0, self.game.player.health))}", True, WHITE)
        surface.blit(hp_text, (20, 20))
        
        wave_text = self.font.render(f"Wave: {self.game.wave_manager.wave_number}", True, WHITE)
        surface.blit(wave_text, (WIDTH - 150, 20))

    def show_game_over(self, surface):
        surface.fill(BG_COLOR)
        game_over_text = self.big_font.render("GAME OVER", True, RED)
        restart_text = self.font.render("Press 'R' to Restart or 'ESC' to Quit", True, WHITE)
        
        surface.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50))
        surface.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 20))
        pygame.display.flip()