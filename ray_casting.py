import pygame
import math

from map import world_map
from settings import HALF_FOV, NUM_RAYS, MAX_DEPTH, DARKGRAY, DELTA_ANGLE, TILE, WHITE, SCALE, HALF_HEIGHT, PROJ_COEF, \
    WIDTH, HEIGHT


def mapping(a, b):
    return a // TILE * TILE, b // TILE * TILE


def ray_casting(screen, player_pos, player_angle):
    x0, y0 = player_pos
    xm, ym = mapping(x0, y0)
    cur_angle = player_angle - HALF_FOV
    depth_v, depth_h = 0, 0

    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)

        # verticals
        x, dx = (xm + TILE, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, WIDTH, TILE):
            depth_v = (x - x0) / cos_a
            y = y0 + depth_v * sin_a

            if mapping(x + dx, y) in world_map:
                break

            x += dx * TILE

        # horizontals
        y, dy = (ym + TILE, 1) if sin_a >= 0 else (ym, -1)

        for i in range(0, HEIGHT, TILE):
            depth_h = (y - y0) / sin_a
            x = x0 + depth_h * cos_a

            if mapping(x, y + dy) in world_map:
                break
            y += dy * TILE

        # projection
        depth = depth_v if depth_v < depth_h else depth_h

        # fix fish eye effect
        depth *= math.cos(player_angle - cur_angle)

        proj_height = PROJ_COEF / depth

        # get color depth
        c = int(255 / (1 + depth * depth * 0.00002))
        color = (c, c // 2, c // 3)
        pygame.draw.rect(
            screen,
            color,
            (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height)
        )

        cur_angle += DELTA_ANGLE
