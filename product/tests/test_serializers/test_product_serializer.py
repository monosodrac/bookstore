from django.test import TestCase
import pytest
from product.models import Product, Category
from product.serializers.product_serializer import ProductSerializer

class TestProductSerializer(TestCase):
    def test_product_serializer(self):
        category = Category.objects.create(
            title= 'produto4',
            slug= '004'
        )

        product= Product.objects.create(
            title= 'produto5',
            price= 500
        )

        product.category.add(category)

        data = ProductSerializer(product).data

        assert data['title'] == 'produto5'
        assert data['price'] == 500
        assert data['category'][0]['title'] == 'produto4'