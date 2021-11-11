import math

import pygame as pg

from map import world_map
from player import Player
from ray_casting import ray_casting
from settings import HEIGHT, WIDTH, BLACK, GREEN, HALF_WIDTH, HALF_HEIGHT, player_pos, DARKGRAY, TILE, ROYAL_BLUE, \
    LIGHT_BLUE


class Game:

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.player = Player()

    def update(self):
        self.player.update()

    def draw(self):
        # pg.draw.circle(self.screen, GREEN, self.player.pos, 12)

        # end_point = self.player.x + WIDTH * math.cos(self.player.angle), \
        #             self.player.x + WIDTH * math.sin(self.player.angle)
        #
        # pg.draw.line(self.screen, GREEN, self.player.pos, end_point)

        # for x, y in world_map:
        #     pg.draw.rect(self.screen, DARKGRAY, (x, y, TILE, TILE), 2)

        pg.draw.rect(self.screen, ROYAL_BLUE, (0, 0, WIDTH, HALF_HEIGHT))
        pg.draw.rect(self.screen, LIGHT_BLUE, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

        ray_casting(self.screen, self.player.pos, self.player.angle)

    def run(self):
        while True:
            [exit() for event in pg.event.get() if event.type == pg.QUIT]
            self.screen.fill(BLACK)

            self.update()
            self.draw()

            pg.display.flip()
            self.clock.tick()


if __name__ == '__main__':
    game = Game()
    game.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
