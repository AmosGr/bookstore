from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from order.factories import OrderFactory, UserFactory
from product.factories import ProductFactory
from order.models import Order

class OrderTestCase(TestCase):

    def test_create_order(self):
        user = UserFactory()
        order = OrderFactory(user=user)
        self.assertEqual(order.user, user)
        self.assertEqual(Order.objects.count(), 1)

    def test_add_products_to_order(self):
        user = UserFactory()
        product1 = ProductFactory()
        product2 = ProductFactory()
        order = OrderFactory(user=user, product=[product1, product2])

        self.assertEqual(order.product.count(), 2)
        self.assertIn(product1, order.product.all())
        self.assertIn(product2, order.product.all())
