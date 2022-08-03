from django.test import TestCase
import reversion

from products.models.product import Product


class ProductTestCase(TestCase):
    def test_create(self):
        product = Product.objects.create(name='python', verbose_name='Python课程', price=0.01)
