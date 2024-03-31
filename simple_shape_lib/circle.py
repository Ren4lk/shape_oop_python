from math import pi

from .shape import Shape


class Circle(Shape):
    def __init__(self, radius) -> None:
        super().__init__(radius)

    def calculate_area(self):
        return self.lines[0] ** 2 * pi
