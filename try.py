from pyshoket import PyShoket

shoket = PyShoket()
response = shoket.make_payment(
    amount=2000,
    customer_name='Stanley Ruheza',
    customer_email='stanleyruheza@gmail.com',
    customer_number='255717610000',
    channel='Tigo'

)

print(response)