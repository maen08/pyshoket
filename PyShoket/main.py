from shoket import PyShoket


""""
Python library for Shoket Payment API
=======================================
Shoket is the payment aggregator which enable live online payments (send and receive money) on web systems.
It allows payments via MNO (Mpesa, TigoPesa, AirtelMoney) on easy way.

"""

pyshoket = PyShoket()

resp = pyshoket.make_payment(
    amount=200,
    customer_name='Stanley Ruheza',
    customer_email='stanleyruheza@gmail.com',
    customer_number='255717614766',
    channel='Tigo'

)

print(resp)