import math

import pygame as pg
from settings import player_pos, player_angle, player_speed


class Player:

    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle

    @property
    def pos(self):
        return self.x, self.y

    def update(self):
        self.movement()


    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.x += player_speed * cos_a
            self.y += player_speed * sin_a
        if keys[pg.K_s]:
            self.x -= player_speed * cos_a
            self.y -= player_speed * sin_a
        if keys[pg.K_a]:
            self.x += player_speed * sin_a
            self.y -= player_speed * cos_a
        if keys[pg.K_d]:
            self.x -= player_speed * sin_a
            self.y += player_speed * cos_a
        if keys[pg.K_LEFT]:
            self.angle -= 0.02
        if keys[pg.K_RIGHT]:
            self.angle += 0.02