## Factory Abstract Class

# Problem: Implement the Factory pattern to create shape objects (e.g., Circle and Square).

# Steps to Solve:

#     Define an abstract Shape class.
#     Create concrete classes for Circle and Square.
#     Write a factory function to return the correct object.

from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstraction Shape class"""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def describe(self) -> str:
        pass


class Circle(Shape):
    """Concrete classes for Circle"""

    def __init__(self, name: str):
        super().__init__(name)

    def describe(self) -> str:
        return f"{self.name} is a Circle"


class Square(Shape):
    """Concrete classes for Square"""

    def __init__(self, name: str):
        super().__init__(name)

    def describe(self) -> str:
        return f"{self.name} is a Square"

def shape_factory(shape_type: str, name: str) -> Shape:
    """Factory function to return the correct object"""
    if shape_type.lower() == "Circle":
        return Circle(name)
    elif shape_type.lower() == "Square":
        return Square(name)
    else:
        raise ValueError("Unknown shape type")

factory = shape_factory("Circle", "MyCircle")

print(factory.describe())
