import pygame
import config


class Snake:
    def __init__(self):
        self.snake_rect = pygame.rect.Rect([200, 200, config.SNAKE_PART_SIZE, config.SNAKE_PART_SIZE])
        self.snake_parts = []
        self.snake_length = len(self.snake_parts) or 1
        self.move_direction = pygame.Vector2(config.SNAKE_MOVE_DISTANCE, 0)

    def move(self):
        self.snake_rect.move_ip(self.move_direction)
        self.snake_parts.append(self.snake_rect.copy())
        self.snake_parts = self.snake_parts[-self.snake_length:]
        return self.snake_parts
