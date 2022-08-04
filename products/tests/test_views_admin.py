from django.test import TestCase
from rest_framework.test import APIRequestFactory

from products.models.product import Product
from products.views.admin import ProductAdminViewSet


class ProductAdminViewSetTestCase(TestCase):
    fixtures = ['service.json']

    def setUp(self):
        self.factory = APIRequestFactory()
        self.object = Product.objects.get(name='python')

    def test_destroy(self):
        request = self.factory.delete("/")
        product_delete_view = ProductAdminViewSet.as_view({'delete': 'destroy'})
        product_delete_view(request, pk=self.object.pk)
        self.assertFalse(self.object.is_active)
