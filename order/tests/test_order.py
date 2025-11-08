from django.test import TestCase
from order.models import Order
from order.serializers.order_serializer import OrderSerializer
from product.models import Product
from django.contrib.auth.models import User

class OrderTestCase(TestCase):
    def test_order(self):
        user = User.objects.create(username='cliente1', email='cliente@client.com')

        product1 = Product.objects.create(
            title='produto1',
            description='001',
            price='200',
            active=True
        )
        product2 = Product.objects.create(
            title='produto2',
            description='002',
            price='300',
            active=True
        )

        order = Order.objects.create(user=user)
        order.product.add(product1, product2)

        data = OrderSerializer(order).data
        self.assertEqual(data["total"], 500)
        self.assertEqual(len(data["product"]), 2)
