import math

WIDTH = 1200
HEIGHT = 800

HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2

# player

player_pos = (HALF_WIDTH, HALF_HEIGHT)
player_angle = 0
player_speed = 1

# map
TILE = 100

FPS = 60

# minimap
MAP_SCALE = 5
MAP_TILE = TILE // MAP_SCALE
MAP_POS = (0, HEIGHT - HEIGHT // MAP_SCALE)

# ray casting settings
FOV = math.pi / 3
HALF_FOV = FOV / 2

NUM_RAYS = 300

MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS

DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEF = DIST * TILE
SCALE = WIDTH // NUM_RAYS

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 0, 220)
YELLOW = (255, 255, 0)
DARKGRAY = (110, 110, 110)
MAGENTA = (255, 0, 255)
ROYAL_BLUE = (65, 105, 225)
LIGHT_BLUE = (173, 216, 230)
