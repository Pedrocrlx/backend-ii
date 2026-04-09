## Session 2 Challenge: Problem: Implement the Observer pattern to notify multiple observers when a subject’s state changes.

## Hint: Create a Subject class that maintains a list of observers.

# Publisher should post new info (Done)
# Observers should receive update every time that Publisher post.

class Publisher:
    """Give to observers new information"""

    stock = {}
    observers = []

    def __init__(self, stock: dict, observers:list):
        self.stock = stock
        self.observers = observers

    def update(self, info:str) -> str:
        return info
    
admin = Publisher({"Stock information": "New stock available"}, ["Observer1", "Observer2"])

print(admin.observers, admin.stock)