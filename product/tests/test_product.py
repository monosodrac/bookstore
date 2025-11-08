from django.test import TestCase
from product.models import Product, Category
from product.serializers.product_serializer import ProductSerializer

class ProductTestCase(TestCase):
    def test_product(self):
        category = Category.objects.create(
            title='produto4',
            slug='004'
        )

        product = Product.objects.create(
            title='produto5',
            price='500'
        )

        product.category.add(category)
        data = ProductSerializer(product).data

        self.assertEqual(data['title'], 'produto5')
        self.assertEqual(data['price'], 500)
        self.assertEqual(data['category'][0]['title'], 'produto4')
