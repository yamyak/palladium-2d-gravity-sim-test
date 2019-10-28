from Object import Object

import pygame


class Display:

    def __init__(self, screen_size, space_size):
        pygame.init()
        self.__screen_size = screen_size
        self.__space_size = space_size
        self.__screen = pygame.display.set_mode((self.__screen_size, self.__screen_size))

    def update(self, objects):
        self.__screen.fill((0, 0, 0))

        for obj in objects:

            x, y = obj.get_location()

            screen_x = int((self.__screen_size / 2) + (x * (self.__screen_size / 2) / self.__space_size))
            screen_y = int((self.__screen_size / 2) - (y * (self.__screen_size / 2) / self.__space_size))

            pygame.draw.circle(self.__screen, (0, 255, 0), (screen_x, screen_y), 1, 0)

        pygame.display.update()
