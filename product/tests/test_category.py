from django.test import TestCase

from product.models import Category
from product.serializers.category_serializer import CategorySerializer


class CategoryTestCase(TestCase):
    def test_category(self):
        category = Category.objects.create(title="produto3", slug="003")

        data = CategorySerializer(category).data
        self.assertEqual(data["title"], "produto3")
        self.assertEqual(data["slug"], "003")
