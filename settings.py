import os
# Root Directory setup
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# Screen Dimensions
WIDTH = 1280
HEIGHT = 720
FPS = 60
TITLE = "Zombie Survival Game"

# Colors (R, G, B)
BG_COLOR = (30, 30, 30)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Player Settings
PLAYER_SPEED = 4
PLAYER_HEALTH = 100

# Bullet Settings
BULLET_SPEED = 15
BULLET_DAMAGE = 25
GUN_COOLDOWN = 200  # milliseconds

# Zombie Settings
ZOMBIE_SPEED = 2
ZOMBIE_HEALTH = 50
ZOMBIE_DAMAGE = 15