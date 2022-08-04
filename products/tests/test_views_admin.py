from django.test import TestCase
from rest_framework.test import APIRequestFactory

from products.models.product import Product
from products.views.admin import ProductAdminViewSet


class ProductAdminViewSetTestCase(TestCase):
    fixtures = ['services.json']

    def setUp(self):
        self.factory = APIRequestFactory()

    def test_destroy(self):
        product = Product.objects.get(name='python')
        request = self.factory.delete("/")
        product_delete_view = ProductAdminViewSet.as_view({'delete': 'destroy'})
        product_delete_view(request, pk=product.pk)
        # Note: 不知道为什么，这里必须要重新查询一次。曾经正常过，其他地方也不需要重新查询。原因未知。
        product = Product.objects.get(name='python')
        self.assertFalse(product.is_active)
