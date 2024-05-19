import pygame
import config
from snake import Snake

screen = pygame.display.set_mode((config.SCREEN_SIZE, config.SCREEN_SIZE))
clock = pygame.time.Clock()
time = None
running = True
begin = True

snake = None
snake_parts = []
move_direction = ""


def draw_grid_lines() -> None:
    for i in range(0, config.SCREEN_SIZE, config.GRID_CELL_SIZE):
        pygame.draw.line(screen, config.GRID_COLOR, (i, 0), (i, config.SCREEN_SIZE))
        pygame.draw.line(screen, config.GRID_COLOR, (0, i), (config.SCREEN_SIZE, i))


def capture_key(key) -> str:
    if key == pygame.K_UP:
        return "UP"
    if key == pygame.K_DOWN:
        return "DOWN"
    if key == pygame.K_LEFT:
        return "LEFT"
    if key == pygame.K_RIGHT:
        return "RIGHT"
    return ""


if __name__ == "__main__":
    while running:
        if begin:
            begin = False
            time = 0
            snake = Snake()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
            if event.type == pygame.KEYDOWN:
                move_direction = capture_key(event.key)

        time_now = pygame.time.get_ticks()
        screen.fill(config.BG_COLOR)
        draw_grid_lines()

        # start moving snake body
        if time_now - time > config.DELAY:
            time = time_now
            snake_parts = snake.move(move_direction)
        # checks if the movement go beyond the wall
        # checks if the snake has touched the body
        [pygame.draw.rect(screen, config.SNAKE_COLOR, snake_part) for snake_part in snake_parts]

        pygame.display.flip()
        clock.tick(config.FPS)
    pygame.quit()
