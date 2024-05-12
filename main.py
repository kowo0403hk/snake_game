import pygame
import config
from snake import Snake

screen = pygame.display.set_mode((config.SCREEN_SIZE, config.SCREEN_SIZE))
clock = pygame.time.Clock()
running = True
begin = True

snake = Snake()


def draw_grid_lines() -> None:
    for i in range(0, config.SCREEN_SIZE, config.GRID_CELL_SIZE):
        pygame.draw.line(screen, config.GRID_COLOR, (i, 0), (i, config.SCREEN_SIZE))
        pygame.draw.line(screen, config.GRID_COLOR, (0, i), (config.SCREEN_SIZE, i))


if __name__ == "__main__":
    while running:
        if begin:
            begin = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

        screen.fill(config.BG_COLOR)
        draw_grid_lines()

        # start moving snake body
        snake_parts = snake.move()
        [pygame.draw.rect(screen, config.SNAKE_COLOR, snake_part) for snake_part in snake_parts]

        pygame.display.flip()
        clock.tick(config.FPS)
    pygame.quit()
