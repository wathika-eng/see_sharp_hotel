import os
from django.conf import settings
from unittest import TestCase
from unittest.mock import patch
from django.test import override_settings
from shop import tests
import unittest


class SettingsTest(TestCase):
    def setUp(self):
        self.env_vars = {
            "SECRET_KEY": "test_secret_key",
            "CLIENT_ID": "test_client_id",
            "CLIENT_SECRET": "test_client_secret",
            "NAME": "test_db_name",
            "USER": "test_db_user",
            "PASSWORD": "test_db_password",
            "HOST": "test_db_host",
            "PORT": "5432",
            "MPESA_ENVIRONMENT": "sandbox",
            "MPESA_CONSUMER_KEY": "test_consumer_key",
            "MPESA_CONSUMER_SECRET": "test_consumer_secret",
            "MPESA_SHORTCODE": "123456",
            "MPESA_EXPRESS_SHORTCODE": "654321",
            "MPESA_SHORTCODE_TYPE": "paybill",
            "MPESA_PASSKEY": "test_passkey",
            "MPESA_INITIATOR_USERNAME": "test_initiator_username",
            "EMAIL_HOST_USER": "test_email_user",
            "EMAIL_HOST_PASSWORD": "test_email_password",
        }

        # Patch environment variables
        patcher = patch.dict(os.environ, self.env_vars)
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_secret_key_setting(self):

        self.assertEqual(settings.SECRET_KEY, self.env_vars["SECRET_KEY"])

    @override_settings(DEBUG=False)
    def test_debug_setting(self):

        self.assertFalse(settings.DEBUG)

    def test_allowed_hosts_setting(self):

        self.assertEqual(settings.ALLOWED_HOSTS, ["*"])

    def test_database_settings(self):

        self.assertEqual(settings.DATABASES["default"]["NAME"], self.env_vars["NAME"])
        self.assertEqual(settings.DATABASES["default"]["USER"], self.env_vars["USER"])
        self.assertEqual(
            settings.DATABASES["default"]["PASSWORD"], self.env_vars["PASSWORD"]
        )
        self.assertEqual(settings.DATABASES["default"]["HOST"], self.env_vars["HOST"])
        self.assertEqual(
            settings.DATABASES["default"]["PORT"], int(self.env_vars["PORT"])
        )

    def test_socialaccount_providers_setting(self):

        google_provider = settings.SOCIALACCOUNT_PROVIDERS["google"]
        self.assertEqual(
            google_provider["APP"]["client_id"], self.env_vars["CLIENT_ID"]
        )
        self.assertEqual(
            google_provider["APP"]["secret"], self.env_vars["CLIENT_SECRET"]
        )

    def test_mpesa_settings(self):

        self.assertEqual(settings.MPESA_ENVIRONMENT, self.env_vars["MPESA_ENVIRONMENT"])
        self.assertEqual(
            settings.MPESA_CONSUMER_KEY, self.env_vars["MPESA_CONSUMER_KEY"]
        )
        self.assertEqual(
            settings.MPESA_CONSUMER_SECRET, self.env_vars["MPESA_CONSUMER_SECRET"]
        )
        self.assertEqual(settings.MPESA_SHORTCODE, self.env_vars["MPESA_SHORTCODE"])
        self.assertEqual(
            settings.MPESA_EXPRESS_SHORTCODE, self.env_vars["MPESA_EXPRESS_SHORTCODE"]
        )
        self.assertEqual(
            settings.MPESA_SHORTCODE_TYPE, self.env_vars["MPESA_SHORTCODE_TYPE"]
        )
        self.assertEqual(settings.MPESA_PASSKEY, self.env_vars["MPESA_PASSKEY"])
        self.assertEqual(
            settings.MPESA_INITIATOR_USERNAME, self.env_vars["MPESA_INITIATOR_USERNAME"]
        )

    def db_tests():
        tests.ProductModelTest()
        tests.ContactModelTest()
        tests.OrdersModelTest()
        tests.OrderUpdateModelTest()

    def test_email_settings(self):

        self.assertEqual(settings.EMAIL_HOST_USER, self.env_vars["EMAIL_HOST_USER"])
        self.assertEqual(
            settings.EMAIL_HOST_PASSWORD, self.env_vars["EMAIL_HOST_PASSWORD"]
        )
        self.assertEqual(settings.EMAIL_USE_TLS, True)
        self.assertEqual(settings.EMAIL_USE_SSL, False)
        self.assertEqual(settings.EMAIL_HOST, "smtp.gmail.com")
        self.assertEqual(settings.EMAIL_PORT, 587)


if __name__ == "__main__":

    unittest.main()
