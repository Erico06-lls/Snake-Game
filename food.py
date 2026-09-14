import random
import pygame

from setting import WIDTH, HEIGHT


class Food:
    def __init__(self, size, occupied_positions):
        self.size = size
        self.position = self.random_position(occupied_positions)

    def random_position(self, occupied_positions):
        while True:
            x = random.randrange(0, WIDTH, self.size)
            y = random.randrange(0, HEIGHT, self.size)

            position = (x, y)

            if position not in occupied_positions:
                return position

    def draw(self, screen):
        x, y = self.position

        pygame.draw.rect(
            screen,
            "red",
            (x, y, self.size, self.size)
        )