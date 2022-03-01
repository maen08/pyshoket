from shoket import PyShoket

pyshoket = PyShoket()

resp = pyshoket.make_payment(
    amount=200,
    customer_name='Stanley Ruheza',
    customer_email='stanleyruheza@gmail.com',
    customer_number='255717614766',
    channel='Tigo'

)

print(resp)