from dataclasses import dataclass
from decouple import config



@dataclass
class url():

    SHOKET_PAYMENT_URL = "https://api.shoket.co/v1/charge/"

    def __init__(self) -> str:
        self.url = self.SHOKET_PAYMENT_URL
        return self.url


def private_key():
    key = config('PRIVATE_KEY')
    return key