from pathlib import Path
import os
from dotenv import load_dotenv
from .secret import UNIQUE_STRING  # generated every 24hrs

load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
false = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "replace_with_yours"
# SECRET_KEY = os.environ["SECRET_KEY"] or UNIQUE_STRING
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = false

ALLOWED_HOSTS = ["hotel.wathika.tech/shop", "127.0.0.1"]

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
# Application definition
CSRF_TRUSTED_ORIGINS = [
    "https://hotel.wathika.tech/shop"
    # "https://classnotes.azurewebsites.net",
    # "https://plainly-intent-dog.ngrok-free.app",
]
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django_daraja",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "rangefilter",
    "shop.apps.ShopConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
SITE_ID = 2

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": ["profile", "email"],
        "APP": {
            "client_id": os.environ["CLIENT_ID"],
            "secret": os.environ["CLIENT_SECRET"],
        },
        "AUTH_PARAMS": {
            "access_type": "online",
        },
    }
}
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
ROOT_URLCONF = "Restaurant_management_system.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["Restaurant_management_system/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "Restaurant_management_system.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ["NAME"],
            "USER": os.environ["USER"],
            "PASSWORD": os.environ["PASSWORD"],
            "HOST": os.environ["HOST"],
            "PORT": int(os.environ["PORT"]),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Africa/Nairobi"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"

# Managing media
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATIC_ROOT = BASE_DIR / "staticfiles"

# STORAGES = {
#     # ...
#     "staticfiles": {
#         "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
#     },
# }

MEDIA_URL = "/media/"
MPESA_ENVIRONMENT = os.environ["MPESA_ENVIRONMENT"]

# Credentials for the daraja app

MPESA_CONSUMER_KEY = os.environ["MPESA_CONSUMER_KEY"]
MPESA_CONSUMER_SECRET = os.environ["MPESA_CONSUMER_SECRET"]

# Shortcode to use for transactions. For sandbox  use the Shortcode 1 provided on test credentials page

MPESA_SHORTCODE = os.environ["MPESA_SHORTCODE"]


MPESA_EXPRESS_SHORTCODE = os.environ["MPESA_EXPRESS_SHORTCODE"]

# Type of shortcode
# Possible values:
# - paybill (For Paybill)
# - till_number (For Buy Goods Till Number)

MPESA_SHORTCODE_TYPE = os.environ["MPESA_SHORTCODE_TYPE"]

# Lipa na MPESA Online passkey
# Sandbox passkey is available on test credentials page
# Production passkey is sent via email once you go live

MPESA_PASSKEY = os.environ["MPESA_PASSKEY"]

# Username for initiator (to be used in B2C, B2B, AccountBalance and TransactionStatusQuery Transactions)

MPESA_INITIATOR_USERNAME = os.environ["MPESA_INITIATOR_USERNAME"]

# Plaintext password for initiator (to be used in B2C, B2B, AccountBalance and TransactionStatusQuery Transactions)

MPESA_INITIATOR_SECURITY_CREDENTIAL = os.environ["MPESA_INITIATOR_SECURITY_CREDENTIAL"]
MPESA_CALLBACK_URL = "https://127.0.0.1:8000/mpesa/callback"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# Host for sending email.
EMAIL_HOST = "smtp.gmail.com"
# Port for sending email.
EMAIL_PORT = 587
# Whether to send SMTP 'Date' header in the local time zone or in UTC.
EMAIL_USE_LOCALTIME = True
# Optional SMTP authentication information for EMAIL_HOST.
EMAIL_HOST_USER = os.environ["EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD = os.environ["EMAIL_HOST_PASSWORD"]
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_SSL_CERTFILE = None
EMAIL_TIMEOUT = None
DEFAULT_FROM_EMAIL = "seasharp <noreply@seasharp.com>"


# SECURITY


if DEBUG:
    pass
else:
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_EXPIRE_AT_BROWSER_CLOSE = True
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
