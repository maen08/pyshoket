from typing import Dict
from utils import private_key, pay_url
import requests
import json


""""
Python library for Shoket Payment API
=======================================
Shoket is the payment aggregator which enable live online payments (send and receive money) on web systems.
It allows payments via MNO (Mpesa, TigoPesa, AirtelMoney) on easy way.
"""


class PyShoket(object):

    def __init__(
        self,
        amount: str = None,
        customer_number: str = None,
        customer_email: str = None,
        customer_name: str = None,
        channel: str = None,
        url: str = None
    ):

        self.__amount = amount
        self.__customer_number = customer_number
        self.__customer_email = customer_email
        self.__customer_name = customer_name
        self.__channel = channel
        self.__url = url

    @property
    def amount(self):
        """
        str: [amount]
        """
        return self.__amount

    @amount.setter
    def amount(self, amount: str):
        """
        set amount to be of type string
        """
        if not isinstance(amount, str):
            raise TypeError(
                f'amount must be str, not {type(amount)}'
            )
        self.__amount = amount

    @property
    def customer_number(self):
        """
        str: [customer_number]
        """
        return self.__customer_number

    @customer_number.setter
    def customer_number(self, customer_number: str):
        """
         set customer_number to be of type string
        """
        if not isinstance(customer_number, str):
            raise TypeError(
                f'customer_number must be str, not {type(customer_number)}'
            )
        self.__customer_number = customer_number

    @property
    def customer_email(self):
        """
        str: [customer_email]
        """
        return self.__customer_email

    @customer_email.setter
    def customer_number(self, customer_email: str):
        """
         set customer_email to be of type string
        """
        if not isinstance(customer_email, str):
            raise TypeError(
                f'customer_email must be str, not {type(customer_email)}'
            )
        self.__customer_email = customer_email

    @property
    def customer_name(self):
        """
        str: [customer_name]
        """
        return self.__customer_name

    @customer_name.setter
    def customer_number(self, customer_name: str):
        """
         set customer_email to be of type string
        """
        if not isinstance(customer_name, str):
            raise TypeError(
                f'customer_name must be str, not {type(customer_name)}'
            )
        self.__customer_name = customer_name

    @property
    def channel(self):
        """
        str: [channel]
        """
        return self.__channel

    @channel.setter
    def channel(self, channel: str):
        """
         set channel to be of type string
        """
        if not isinstance(channel, str):
            raise TypeError(
                f'channel must be str, not {type(channel)}'
            )
        self.__channel = channel

    @property
    def url(self):
        """
        str: [channel]
        """
        return self.__url

    @url.setter
    def url(self):
        self.__url = pay_url()
        return self.__url

    @property
    def headers(self):
        headers = {
            'Authorization': private_key(),
            'Content-Type': 'application/json'
        }

        return headers

    def make_payment(
        self,
        amount,
        customer_name,
        customer_email,
        customer_number,
        channel

    ):

        payload = json.dumps({
            "amount": amount,
            "customer_name": customer_name,
            "customer_email": customer_email,
            "customer_number": customer_number,
            "channel": channel
        })

        res = requests.post(
            data=payload,
            headers=self.headers,
            url=pay_url()
        )

        if res.status_code == 200:
            data = {
                'detail': res.content,
                'message': 'Successful payment',
                'status_code': res.status_code
            }

            return data
        else:
            data = {
                'detail': res.content,
                'message': 'Errors!, Unsuccessful payment',
                'status_code': res.status_code
            }
        return data


