import pygame

class Snake:
    def __init__(self):
        self.size = 20
        self.body = [
            (100, 100),
            (80, 100),
            (60, 100)
        ]

        self.dx = 1
        self.dy = 0

    def change_direction(self, dx, dy):
        if (dx, dy) != (-self.dx, -self.dy):
            self.dx = dx
            self.dy = dy

    def next_position(self):
        head_x, head_y = self.body[0]

        return (
            head_x + self.dx * self.size,
            head_y + self.dy * self.size
        )

    def move(self, grow=False):
        new_head = self.next_position()

        self.body.insert(0, new_head)

        if not grow:
            self.body.pop()

    def get_head(self):
        return self.body[0]

    def draw(self, screen):
        for x, y in self.body:
            pygame.draw.rect(
                screen,
                "green",
                (x, y, self.size, self.size)
            )