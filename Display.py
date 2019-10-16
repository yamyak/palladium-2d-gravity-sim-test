from Object import Object

import pygame


class Display:

    def __init__(self):
        pygame.init()
        self.__screen = pygame.display.set_mode((500, 500))

    def update(self, objects):
        self.__screen.fill((0, 0, 0))

        for obj in objects:

            x, y = obj.get_location()

            screen_x = int(250 + (x * 250 / 2.5e11))
            screen_y = int(250 - (y * 250 / 2.5e11))

            pygame.draw.circle(self.__screen, (0, 255, 0), (screen_x, screen_y), 1, 0)

        pygame.display.update()
