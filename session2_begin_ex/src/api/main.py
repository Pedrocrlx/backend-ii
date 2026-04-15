from fastapi import FastAPI
from payments.adapter import PaymentBaseAdapter
from payments.factory import PaymentProviderFactory
from schemas.models import Payment

app = FastAPI()

@app.post("/pay")
async def process_payment(payload: Payment):
    provider:PaymentBaseAdapter = PaymentProviderFactory().get_provider(name=payload.provider)
    await provider.pay(payload=payload.payment_payload)
    return { "Payment success": 1 }