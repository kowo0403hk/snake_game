import pygame
from pygame import Rect
import config
from snake import Snake
from random import randrange

screen = pygame.display.set_mode((config.SCREEN_SIZE, config.SCREEN_SIZE))
clock = pygame.time.Clock()
time = None
running = True
in_game = False
generated_apple = False

snake = None
snake_parts = []
move_direction = None

apple_rect = None


def draw_grid_lines() -> None:
    for i in range(0, config.SCREEN_SIZE, config.GRID_CELL_SIZE):
        pygame.draw.line(screen, config.GRID_COLOR, (i, 0), (i, config.SCREEN_SIZE))
        pygame.draw.line(screen, config.GRID_COLOR, (0, i), (config.SCREEN_SIZE, i))


def generate_apple() -> Rect:
    return pygame.rect.Rect([randrange(0, config.SCREEN_SIZE, config.GRID_CELL_SIZE),
                             randrange(0, config.SCREEN_SIZE, config.GRID_CELL_SIZE), config.APPLE_SIZE,
                             config.APPLE_SIZE])


def hits_border(snake_head: Rect) -> bool:
    return (snake_head.left < 0 or snake_head.right > config.SCREEN_SIZE
            or snake_head.top < 0 or snake_head.bottom > config.SCREEN_SIZE)


def hits_body(snake_parts_rects: list[Rect]) -> bool:
    return len(snake_parts_rects) != len(set(snake_part.center for snake_part in snake_parts_rects))


if __name__ == "__main__":
    while running:
        if not in_game:
            in_game = True
            time = 0
            snake = Snake()

        if not generated_apple:
            apple_rect = generate_apple()
            generated_apple = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
            if event.type == pygame.KEYDOWN:
                move_direction = event.key

        time_now = pygame.time.get_ticks()
        screen.fill(config.BG_COLOR)
        draw_grid_lines()

        # start moving snake body
        if time_now - time > config.DELAY:
            time = time_now
            snake_parts = snake.move(move_direction)

        pygame.draw.rect(screen, config.APPLE_COLOR, apple_rect, 0, 10)
        [pygame.draw.rect(screen, config.SNAKE_COLOR, snake_part, 8, 4) for snake_part in snake_parts]

        if hits_border(snake.snake_head) or hits_body(snake_parts):
            in_game = False
            move_direction = None

        # apple consumption
        if snake.snake_head.center == apple_rect.center:
            snake.consumes_apple()
            generated_apple = False

        pygame.display.flip()
        clock.tick(config.FPS)
    pygame.quit()
