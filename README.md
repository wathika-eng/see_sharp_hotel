# **A hotel ordering website made with Django**

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
