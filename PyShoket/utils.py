from dataclasses import dataclass
from decouple import config



def pay_url():
    SHOKET_PAYMENT_URL = "https://api.shoket.co/v1/charge/"
    return SHOKET_PAYMENT_URL


def private_key():
    key = config('PRIVATE_KEY')
    return key