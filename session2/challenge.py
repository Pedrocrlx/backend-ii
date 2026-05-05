## Session 2 Challenge: Problem: Implement the Observer pattern to notify multiple observers when a subject’s state changes.


products = ["Product 1", "Product 2", "Product 3"]

class Publisher:
    """Give to observers new information"""

    def __init__(self,):
        self.observers = []

    def subscribe(self, observer:Observer):
        self.observers.append(observer)
        print(f"{observer.name} has subscribed to updates.")

    def update(self, info:str) -> str:
        products.append(info)
        print(f"Updated products: {products}")
        for observer in self.observers:
            observer.update(info)
        return info
    
class Observer:
    """Receive information from the publisher"""
    def __init__(self, name: str):
        self.name = name

    def update(self, info:str):
        print(f"{self.name} received update: {info}")

admin = Publisher()

admin.subscribe(Observer("Observer 1"))

admin.update("Product 4")

print(admin.observers[0].name)

## falta o método unsubscribe para remover um observer da lista de observadores do publisher.
