import pygame
import config

screen = pygame.display.set_mode((config.SCREEN_SIZE, config.SCREEN_SIZE))
clock = pygame.time.Clock()
running = True


def main():
    global running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill('orange')
        pygame.display.flip()
        clock.tick(config.FPS)
    pygame.quit()


if __name__ == "__main__":
    main()
