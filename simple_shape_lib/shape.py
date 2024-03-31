from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def __init__(self, *lines) -> None:
        if not all(isinstance(line, (int, float)) for line in lines):
            raise ValueError("Values must be numeric")

        if any(line <= 0 for line in lines):
            raise ValueError("Invalid shape")

        super().__init__()
        self.lines = list(lines)

    @abstractmethod
    def calculate_area():
        pass
