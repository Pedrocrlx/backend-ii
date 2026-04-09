## Factory Abstract Class

# Problem: Implement the Factory pattern to create shape objects (e.g., Circle and Square).

# Steps to Solve:

#     Define an abstract Shape class.
#     Create concrete classes for Circle and Square.
#     Write a factory function to return the correct object.


class FactoryShape:
    """Creation of circle and square shapes"""
    
    def __init__(self, name: str):
        self.name = name

    def create_circle(name: str) -> str:
        return f"{name} circle was created"
    
    def create_square(name: str) -> str:
        return f"{name} square was created"

circle = FactoryShape.create_circle("Pedro Santos")
square = FactoryShape.create_square("Jorge Alves")

print(f"{circle} and {square}")