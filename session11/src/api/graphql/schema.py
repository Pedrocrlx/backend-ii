from pydantic import BaseModel
import strawberry
from api.schemas.models import Payment

@strawberry.type
class PaymentType(BaseModel):
    user: str
    email: str
    payment_method: str

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello from GraphQL!"

    # @strawberry.field
    # def get_payment(self, user: str) -> PaymentType:
    #     return PaymentType(user=user, email="test@example.com", payment_method="credit_card")

# @strawberry.type
# class Mutation:
#     @strawberry.mutation
#     def process_payment(self, user: str, email: str, payment_method: str) -> PaymentType:
#         return PaymentType(user=user, email=email, payment_method=payment_method)

schema = strawberry.Schema(query=Query)
