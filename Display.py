from Object import Object

import pygame


class Display:

    # initialize display with pygame and simulation size
    def __init__(self, screen_size, space_size):
        pygame.init()
        self.__screen_size = screen_size
        self.__space_size = space_size
        self.__screen = pygame.display.set_mode((self.__screen_size, self.__screen_size))

    # given lists of solar system objects, update their positions on the display
    def update(self, objects):
        # blank out the display screen
        self.__screen.fill((0, 0, 0))

        # iterate through all objects
        for obj in objects:

            # get object location
            x, y = obj.get_location()

            # translate simulation location coordinates into display coordinates
            screen_x = int((self.__screen_size / 2) + (x * (self.__screen_size / 2) / self.__space_size))
            screen_y = int((self.__screen_size / 2) - (y * (self.__screen_size / 2) / self.__space_size))

            # draw object on display screen
            pygame.draw.circle(self.__screen, (0, 255, 0), (screen_x, screen_y), 1, 0)

        # update the display screen
        pygame.display.update()
