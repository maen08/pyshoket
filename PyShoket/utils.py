from dataclasses import dataclass
from decouple import config


class CustomerDetails():
    """
    Required details in order to make payment
    """
    amount: str 
    customer_number: str         
    customer_email: str
    customer_name: str 
    channel: str 
    url: str 



def pay_url():
    SHOKET_PAYMENT_URL = "https://api.shoket.co/v1/charge/"
    return SHOKET_PAYMENT_URL


def private_key():
    key = config('PRIVATE_KEY')
    return key