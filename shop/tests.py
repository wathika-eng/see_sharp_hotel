from django.test import TestCase
from django.utils import timezone
from .models import Product, Contact, Orders, OrderUpdate


class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            product_name="Test Product",
            category="Test Category",
            subcategory="Test Subcategory",
            price=100,
            desc="Test description",
            pub_date=timezone.now(),
            image="",
        )

    def test_product_creation(self):
        self.assertEqual(self.product.product_name, "Test Product")
        self.assertEqual(self.product.category, "Test Category")
        self.assertEqual(self.product.subcategory, "Test Subcategory")
        self.assertEqual(self.product.price, 100)
        self.assertEqual(self.product.desc, "Test description")

    def test_product_str(self):
        self.assertEqual(str(self.product), "Test Product")


class ContactModelTest(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            name="Test User",
            email="test@example.com",
            phone="1234567890",
            desc="Test contact description",
            timestamp=timezone.now(),
        )

    def test_contact_creation(self):
        self.assertEqual(self.contact.name, "Test User")
        self.assertEqual(self.contact.email, "test@example.com")
        self.assertEqual(self.contact.phone, "1234567890")
        self.assertEqual(self.contact.desc, "Test contact description")

    def test_contact_str(self):
        self.assertEqual(str(self.contact), "Test User")


class OrdersModelTest(TestCase):
    def setUp(self):
        self.order = Orders.objects.create(
            items_json="{'item1': 1, 'item2': 2}",
            userId=1,
            amount=200,
            name="Test Buyer",
            email="buyer@example.com",
            city="Test City",
            estate="Test Estate",
            apartment="Test Apartment",
            phone="0987654321",
            timestamp=timezone.now(),
        )

    def test_order_creation(self):
        self.assertEqual(self.order.items_json, "{'item1': 1, 'item2': 2}")
        self.assertEqual(self.order.userId, 1)
        self.assertEqual(self.order.amount, 200)
        self.assertEqual(self.order.name, "Test Buyer")
        self.assertEqual(self.order.email, "buyer@example.com")
        self.assertEqual(self.order.city, "Test City")
        self.assertEqual(self.order.estate, "Test Estate")
        self.assertEqual(self.order.apartment, "Test Apartment")
        self.assertEqual(self.order.phone, "0987654321")


class OrderUpdateModelTest(TestCase):
    def setUp(self):
        self.order_update = OrderUpdate.objects.create(
            order_id=1, update_desc="Order has been shipped", timestamp=timezone.now()
        )

    def test_order_update_creation(self):
        self.assertEqual(self.order_update.order_id, 1)
        self.assertEqual(self.order_update.update_desc, "Order has been shipped")

    def test_order_update_str(self):
        self.assertEqual(str(self.order_update), "Order has been shipped")
