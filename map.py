import pygame as pg
from settings import WIDTH, TILE, MAP_TILE

text_map = [
    'WWWWWWWWWWWW',
    'W..........W',
    'W...W......W',
    'W.......W..W',
    'W..W.......W',
    'W......W...W',
    'W..........W',
    'WWWWWWWWWWWW',
]

world_map = set()
minimap = set()

for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i * TILE, j * TILE))
            minimap.add((i * MAP_TILE, j * MAP_TILE))
