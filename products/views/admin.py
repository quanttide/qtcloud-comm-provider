# -*- coding: utf-8 -*-
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.viewsets import ModelViewSet

from products.models.product import Product
from products.serializers.base import ProductSerializer


class ProductAdminViewSet(ModelViewSet):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        # TODO: 根据Product.type选择不同的serializer_class
        # Note: 备选工具 https://github.com/MattBroach/DjangoRestMultipleModels
        return ProductSerializer

    def destroy(self, request, *args, **kwargs):
        """
        修改默认删除行为。修改标记is_active=False
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(instance=self.get_object(), data={'is_active': False})
        serializer.delete()
        return Response(status=HTTP_204_NO_CONTENT)
