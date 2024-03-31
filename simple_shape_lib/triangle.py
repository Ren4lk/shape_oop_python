from .shape import Shape


class Triangle(Shape):
    def __init__(self, *sides) -> None:
        super().__init__(*sides)

        if len(sides) != 3:
            raise ValueError("Triangle requires 3 sides")

        if max(sides) >= sum(sides) - max(sides):
            raise ValueError("Invalid triangle")

    def calculate_area(self):
        p = sum(self.lines) / 2
        return (
            p * (p - self.lines[0]) * (p - self.lines[1]) * (p - self.lines[2])
        ) ** 0.5

    def is_right_triangle(self):
        sides = sorted(self.lines)
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2
