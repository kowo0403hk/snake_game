import pygame
from pygame import Vector2
import config
from random import randrange


class Snake:
    def __init__(self):
        self.snake_rect = pygame.rect.Rect(
            [randrange(0, config.SCREEN_SIZE, config.GRID_CELL_SIZE),
             randrange(0, config.SCREEN_SIZE, config.GRID_CELL_SIZE),
             config.SNAKE_PART_SIZE,
             config.SNAKE_PART_SIZE])
        self.snake_parts = []
        self.snake_length = len(self.snake_parts) or 1
        self.move_direction = {
            "UP": Vector2(0, -config.SNAKE_MOVE_DISTANCE),
            "DOWN": Vector2(0, config.SNAKE_MOVE_DISTANCE),
            "LEFT": Vector2(-config.SNAKE_MOVE_DISTANCE, 0),
            "RIGHT": Vector2(config.SNAKE_MOVE_DISTANCE, 0)
        }

    def move(self, key_direction: str):
        valid_direction = self.move_direction.get(key_direction, None)
        # need to test 2 boundaries
        # 1. cannot go opposite direction
        # 2. cannot accept other keys input
        # if 1 or 2 happens, keeps going the current direction
        # 3. if we go beyond the screen, it stops
        if valid_direction:
            self.snake_rect.move_ip(valid_direction)
        self.snake_parts.append(self.snake_rect.copy())
        self.snake_parts = self.snake_parts[-self.snake_length:]
        return self.snake_parts

    def consumes_apple(self):
        self.snake_length += 1
