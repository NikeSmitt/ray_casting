import math

import pygame

import settings
from map import minimap
from player import Player
from ray_casting import ray_casting


class Drawing:
    def __init__(self, screen: pygame.display, minimap: pygame.Surface):
        self.screen = screen
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.map_sc = minimap

    def background(self):
        pygame.draw.rect(self.screen, settings.ROYAL_BLUE, (0, 0, settings.WIDTH, settings.HALF_HEIGHT))
        pygame.draw.rect(self.screen, settings.LIGHT_BLUE, (0, settings.HALF_HEIGHT, settings.WIDTH, settings.HALF_HEIGHT))

    def world(self, position: (int, int), angle: int):
        """
        Draw a whole world
        :param position:
        :param angle:
        :return:
        """
        ray_casting(self.screen, position, angle)

    def fps(self, clock: pygame.time.Clock):
        """
        Display fps on screen
        :param clock: pygame.time.Clock
        :return: None
        """
        fps_value = str(int(clock.get_fps()))
        fps_render = self.font.render(fps_value, False, settings.RED)

        # add fps on right top corner
        self.screen.blit(fps_render, (settings.WIDTH - 65, 5))

    def minimap(self, player: Player):
        self.map_sc.fill(settings.BLACK)

        map_x, map_y = player.x // settings.MAP_SCALE, player.y // settings.MAP_SCALE
        pygame.draw.circle(self.map_sc, settings.RED, (map_x, map_y), 5)

        end_point = map_x + 12 * math.cos(player.angle), map_y + 12 * math.sin(player.angle)
        pygame.draw.line(self.map_sc, settings.GREEN, (map_x, map_y), end_point)

        for x, y in minimap:
            pygame.draw.rect(self.map_sc, settings.GREEN, (x, y, settings.MAP_TILE, settings.MAP_TILE))

        self.screen.blit(self.map_sc, settings.MAP_POS)
