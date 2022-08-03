# -*- coding: utf-8 -*-

from rest_framework import serializers
from products.models.bundle import Bundle, BundleItem


class BundleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BundleItem
        fields = "__all__"


class BundleSerializer(serializers.ModelSerializer):
    """
    订单模型序列化类

    TODO: 增加price字段，取Price表的最新结果；具体根据版本管理实现方式决定。
    """
    items = BundleItemSerializer(many=True)

    class Meta:
        model = Bundle
        fields = "__all__"
