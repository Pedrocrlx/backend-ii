from adapter import PaymentBaseAdapter

class MBWayPayment(PaymentBaseAdapter):
    async def pay(self, payload: dict) -> bool:
        # Implement the logic to process the payment using MBWay
        # For example, you can use an HTTP client to send a request to the MBWay API
        # and handle the response accordingly.
        return True  # Return True if the payment was successful, False otherwise
    
class PayPalPayment(PaymentBaseAdapter):
    async def pay(self, payload: dict) -> bool:
        # Implement the logic to process the payment using PayPal
        # For example, you can use an HTTP client to send a request to the PayPal API
        # and handle the response accordingly.
        return True  # Return True if the payment was successful, False otherwise