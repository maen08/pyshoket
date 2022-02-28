from dataclasses import dataclass

@dataclass
class url():

    SHOKET_PAYMENT_URL = "https://api.shoket.co/v1/charge/"

    def __init__(self) -> None:
        self.url = self.SHOKET_PAYMENT_URL
        return self.url
