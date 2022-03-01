# pyshoket
- A Python wrapper for Shoket API. 
- Make online payments easy with `pyshoket`, connecting MNO such as Tigo (Tigopesa),
Halotel (Halopesa) and Airtel (Airtel money)

# Installation
- Installing pyshoket using `pip`
```
pip install pyshoket
```

- OR You can also install pyshoket from github repository.
```
git clone https://github.com/maen08/pyshoket

```

# Setup environment variables   
To perform payments with Shoket, you need to pass `PRIVATE_KEY` in the request. Its already handled in this wrapper, what you need to do is to keep your Shoket key private.

- You can receive your private key [here](https://dashboard.shoket.co/) after signup in the Shoket account.
- In the root directory of your project, create `.env` file to store your key
```
PRIVATE_KEY=mpBsk_icAldgTTvXXXXXXXXXXXXXXXX
```
NB: No space between equal sign

# Usage
To enable payments in your project with `pyshoket`, this is how you can do it.

```
from pyshoket import Pyshoket

shoket = Pyshoket()
response = shoket.make_payment(
    amount=2000,
    customer_name='Stanley Ruheza',
    customer_email='stanleyruheza@gmail.com',
    customer_number='255717610000',
    channel='Tigo'

)

print(response)

```

If we check the response of the above request (Successful request), it will be something like this:
```
# Response of successful request


{
    "Status": "success" ,
    "customer" {
        "customer_name": "376FcD3gbidW",
        "email": "stanleyruheza@gmail.com",
        "id": 64043
    },
    "data": {
        "amount": 2000,
        "channel": "Tigo",
        "currency": "TSH",
        "number_used": "255717610000",
        "status": "Success",
        "transaction_date": "2022-03-01 15:08:59.917691"
    },
    "message": "Transaction is completed",
    "reference": "adz49dS428b7kbDTdG4MN"
}

```



# Contribution
Pyshoket is an open source project so feel free to contribute. You can contribute in various ways, including:
- Fixing typos in the codes and the README document.
- Add more features on the project 
- Resolve raised issues
- Write use cases
- Improve documentation

# Credits
Credits to all contributors of Pyshoket. Your work is worthy.
- [maen08](https://github.com/maen08/) - maintainer
- Contributors

# Give it a star
Share the project with your team, give it a star and use it.

# Licence
Pyshoket is an Open Source project under [MIT licence](https://github.com/maen08/pyshoket/blob/master/LICENCE)

