from payments.adapter import PaymentBaseAdapter
from payments.providers import MBWayPayment, PayPalPayment


class PaymentProviderFactory:
    """Factory class to create payment provider instances based on the provider name."""
    REGISTRY: dict[str, type[PaymentBaseAdapter]] = {
        "mbway": MBWayPayment,
        "paypal": PayPalPayment
    }

    def get_payment_provider(self, name: str)-> PaymentBaseAdapter:

        provider = self.REGISTRY.get(name, None)
        
        if not provider:
             raise ValueError(f"Unsupported payment provider: {name}")
        
        return provider()
      