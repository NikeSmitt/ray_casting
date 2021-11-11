import math

import pygame

from map import world_map
from player import Player
import settings
from drawing import Drawing


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        self.minimap_sc = pygame.Surface((settings.WIDTH // settings.MAP_SCALE, settings.HEIGHT // settings.MAP_SCALE))
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.drawing = Drawing(self.screen, self.minimap_sc)

    def update(self):
        self.player.update()

    def draw(self):
        self.drawing.background()
        self.drawing.world(self.player.pos, self.player.angle)
        self.drawing.fps(self.clock)
        self.drawing.minimap(self.player)

    def run(self):
        while True:
            [exit() for event in pygame.event.get() if event.type == pygame.QUIT]
            self.screen.fill(settings.BLACK)

            self.update()
            self.draw()

            pygame.display.flip()
            self.clock.tick()


if __name__ == '__main__':
    game = Game()
    game.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
