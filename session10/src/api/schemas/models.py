from pydantic import BaseModel

class Payment(BaseModel):
    user:str
    email: str
    cart: list[dict]
    payment_method: str
    payment_payload: dict
