# **A hotel ordering website made with Django**

Sample video demo => https://mega.nz/file/mO4V0ISA#INd-lyXZIfuMFrvzbjgdzIr4wWGd1Fvau8TYK72BIB8

Images => https://mega.nz/file/eOoXVaqT#yNPa51Ax418XK71cBv_hXZ1wfgXC4CL4Athbvm0Wg_0

Mobile view => https://mega.nz/file/qSAlESTC#HEEUVQgCX5tKWiGwWOcZkXiYxnTo3LTFSTbgCQ_cFXk

Schema =>

Live website =>

Logins:
  Username: admin2
  Password: changeme
  
## Features
1. Login with Google supported
2. Able to track orders
3. Mpesa stk push with correct amount
4. Sends confirmation order to clients phone number(SMS) and Email
5. Forgot password functionality
6. Request special orders to chef(Able to receive them in the admin panel)

# Get started with the app locally

```
git clone 
```

```
virtualenv .venv
```

```
source .venv/bin/activate
```

Ensure the virtual environment is activated!
```
pip install -r requirements.txt 
```

Rename the .env.local to .env

Get all required variables from cloud console, daraja api and Gmail settings

```
python manage.py makemigrations
```

(without --run-syncdb `shops` table won't be created as seen here  )
```
python manage.py migrate  --run-syncdb 
```

```
python manage,py runserver
```
Optionally:
You can create an admin account by:
```
python manage.py createsuperuser
```

To run tests:
```
python manage.py test (security && configs)
```

```
python manage.py test shop.tests (database)
```

[X] SMS and Email delivery working

[X] Mpesa STK Push

[X] Google Login and Reset password

# Enquiries

https://stackoverflow.com/questions/5420789/how-to-install-psycopg2-with-pip-on-python - solves pyscopg2 installation error