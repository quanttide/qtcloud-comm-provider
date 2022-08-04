from django.test import TestCase

from products.models.producer import Producer
from products.models.product import Product, Price


class ProductTestCase(TestCase):
    def test_create(self):
        producer = Producer.objects.create()
        product = Product.objects.create(name='python', verbose_name='Python课程', producer=producer)


class PriceTestCase(TestCase):
    def setUp(self):
        producer = Producer.objects.create()
        product = Product.objects.create(name='python', verbose_name='Python课程', producer=producer)
        price1 = Price.objects.create(product=product, price=0.1)
        price2 = Price.objects.create(product=product, price=0.2)

    def test_get_current_price(self):
        price = Price.objects.latest()
        self.assertEqual(0.2, float(price.price))
