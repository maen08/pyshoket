from decouple import config


def pay_url():
    """
    method to setup a base url used in Shoket Payment
    """
    SHOKET_PAYMENT_URL = "https://api.shoket.co/v1/charge/"
    return SHOKET_PAYMENT_URL


def private_key():
    """
    a method to setup a private key which is passed as a paramenter
    in a payment request
    """
    key = config('PRIVATE_KEY')
    return key
