from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from api.payments.adapter import PaymentBaseAdapter
from api.payments.factory import PaymentProviderFactory
from api.schemas.models import Payment
from api.graphql.schema import schema

app = FastAPI()

@app.post("/pay")
async def process_payment(payload: Payment):
    provider:PaymentBaseAdapter = PaymentProviderFactory().get_payment_provider(name=payload.payment_method)
    await provider.pay(payload=payload.payment_payload)
    return  {"Payment success": True, "User": payload.user, "Cart": payload.cart, "Payment Method": payload.payment_method }

app.include_router(GraphQLRouter(schema), prefix="/graphql")