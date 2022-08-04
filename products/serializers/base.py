# -*- coding: utf-8 -*-
from decimal import Decimal

from rest_framework import serializers

from products.models.producer import Producer
from products.models.product import Product, Price


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        exclude = ['id']
        extra_kwargs = {
            'name': {'validators': []},
            'type': {'required': False}
        }


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        exclude = ['id']


class ProductSerializer(serializers.ModelSerializer):
    producer = ProducerSerializer()
    price = serializers.DecimalField(max_digits=10, decimal_places=2, allow_null=True)
    price_models = PriceSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['price'] = Decimal(data.pop('price_models')[-1]['price'])
        return data

    def create(self, validated_data):
        # 获取Producer实例
        validated_data['producer'] = Producer.objects.get(name=validated_data.pop('producer')['name'])
        # 创建Product实例
        price = validated_data.pop('price')
        instance = super().create(validated_data)
        # 创建Price实例
        Price.objects.create(price=price, product=instance)
        return instance

    def update(self, instance, validated_data):
        # 如果价格变化，更新价格
        if 'price' in validated_data:
            current_price = Price.objects.filter(product=instance).latest().price
            if current_price != validated_data['price']:
                Price.objects.create(product=instance, price=validated_data['price'])
        # 正常更新
        return super().update(instance, validated_data)

    def delete(self):
        """
        自定义方法。标记is_active=False代替真实删除
        """
        return self.update(self.instance, {'is_active': False})
