import pygame
import math

from map import world_map
from settings import HALF_FOV, NUM_RAYS, MAX_DEPTH, DARKGRAY, DELTA_ANGLE, TILE, WHITE, SCALE, HALF_HEIGHT, PROJ_COEF


def ray_casting(screen, player_pos, player_angle):
    cur_angle = player_angle - HALF_FOV
    x0, y0 = player_pos

    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)

        for depth in range(MAX_DEPTH):
            x = x0 + depth * cos_a
            y = y0 + depth * sin_a

            # pygame.draw.line(screen, DARKGRAY, player_pos, (x, y), 2)
            if (x // TILE * TILE, y // TILE * TILE) in world_map:
                proj_height = PROJ_COEF / depth

                # fix fish eye effect
                depth *= math.cos(player_angle - cur_angle)

                # get color depth
                c = int(255 / (1 + depth * depth * 0.00001))
                color = (c, c//2, c//3)
                pygame.draw.rect(
                    screen,
                    color,
                    (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height)
                )
                break

        cur_angle += DELTA_ANGLE
