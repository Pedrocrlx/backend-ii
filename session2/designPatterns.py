## Factory Abstract Class

# Problem: Implement the Factory pattern to create shape objects (e.g., Circle and Square).

# Steps to Solve:

#     Define an abstract Shape class.
#     Create concrete classes for Circle and Square.
#     Write a factory function to return the correct object.

from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstraction Shape class"""
    def __init__(self,name: str) -> str:
        return name
        
    @abstractmethod
    def describe(self) -> str:
        pass
    
class Circle(Shape):
    """Concrete classes for Circle"""
    def describe(self) -> str:
        return self.name
    
class Square:
    """Concrete classes for Square"""
    def describe(self) -> str:
        return self.name

class FactoryShape:
    """Creation of circle and square shapes"""
    factory_stock = {}
    
    def create_circle(self,name: str) -> str:
        shape_type = "Circle"
        FactoryShape.factory_stock.setdefault(name, shape_type)
        return f"{name} circle was created type:{shape_type}"
    
    def create_square(self,name: str) -> str:
        shape_type = "Square"
        FactoryShape.factory_stock.setdefault(name, shape_type)
        return f"{name} square was created type: {shape_type}"
    
factory = FactoryShape()

circle = factory.create_circle("Pedro Redondo")
square = factory.create_square("Pedro Quadrado")

print(circle.describe)

# keys = FactoryShape.factory_stock.keys()
# values = FactoryShape.factory_stock.values()
# print(f"We got created already: {keys} and their types are: {values}")