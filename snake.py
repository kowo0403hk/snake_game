import pygame
from pygame import Rect
from pygame import Vector2
import config
from random import randrange


class Snake:
    def __init__(self):
        self.snake_head: Rect = pygame.rect.Rect(
            [randrange(0, config.SCREEN_SIZE, config.GRID_CELL_SIZE),
             randrange(0, config.SCREEN_SIZE, config.GRID_CELL_SIZE),
             config.SNAKE_PART_SIZE,
             config.SNAKE_PART_SIZE])
        self.snake_parts: list[Rect] = []
        self.snake_length = len(self.snake_parts) or 1
        self.current_direction = Vector2(0, 0)

    def move(self, key_event: int) -> list[Rect]:
        valid_movement = None
        if key_event == pygame.K_UP and not self.current_direction[1] > 0:
            valid_movement = Vector2(0, -config.SNAKE_MOVE_DISTANCE)
        if key_event == pygame.K_DOWN and not self.current_direction[1] < 0:
            valid_movement = Vector2(0, config.SNAKE_MOVE_DISTANCE)
        if key_event == pygame.K_LEFT and not self.current_direction[0] > 0:
            valid_movement = Vector2(-config.SNAKE_MOVE_DISTANCE, 0)
        if key_event == pygame.K_RIGHT and not self.current_direction[0] < 0:
            valid_movement = Vector2(config.SNAKE_MOVE_DISTANCE, 0)

        if valid_movement:
            self.snake_head.move_ip(valid_movement)
            self.current_direction = valid_movement
        else:
            self.snake_head.move_ip(self.current_direction)
        self.snake_parts.append(self.snake_head.copy())
        self.snake_parts = self.snake_parts[-self.snake_length:]
        return self.snake_parts

    def consumes_apple(self) -> None:
        self.snake_length += 1
