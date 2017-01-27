from enum import Enum
from Block import *
from Constants import *
import numpy as np
import math


class Snake:
    def __init__(self, game_map, head, gen):
        self.game_map = game_map
        self.direction = gen[0]
        self.body = head
        self.gen = gen
        self.fitness = 0
    
    def calcualte_fitness(self):
        self.fitness =math.sqrt(GOAL[0]**2+GOAL[1]**2) - math.sqrt((GOAL[0]-self.body.position.x)**2+(GOAL[1]-self.body.position.y)**2)
        self.body.type=BlockType.Normal
    def move(self, step):
        self.direction = self.gen[step]
        head = self.body
        to_pos = [
            int(head.position.x / BLOCK_SIZE),
            int(head.position.y / BLOCK_SIZE)
        ]
        to_pos[0] = to_pos[0] + self.direction[0]
        if to_pos[0] >= MAP_HEIGHT:
            to_pos[0] = to_pos[0] - MAP_HEIGHT
        if to_pos[0] < 0:
            to_pos[0] = to_pos[0] + MAP_HEIGHT
        to_pos[1] = to_pos[1] + self.direction[1]
        if to_pos[1] >= MAP_WIDTH:
            to_pos[1] = to_pos[1] - MAP_WIDTH
        if to_pos[1] < 0:
            to_pos[1] = to_pos[1] + MAP_WIDTH
        to = self.game_map[to_pos[0]][to_pos[1]]
        if to.type == BlockType.Wall:
            pass
        else:
            to.type = BlockType.Snake
            self.body.type = BlockType.Normal
            self.body = to