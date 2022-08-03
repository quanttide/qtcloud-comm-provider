"""
商品数据模型
"""

import uuid

from django.db import models

# from products.models.producer import Producer


class ProductTypeChoices(models.TextChoices):
    """
    商品类型
    """
    goods = 'goods', '实物商品'
    service = 'service', '服务'
    bundle = 'bundle', '商品组合'


class Product(models.Model):
    """
    商品（也称产品）
    """
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, verbose_name='商品ID')
    name = models.CharField(max_length=64, unique=True, verbose_name='商品名称')
    verbose_name = models.CharField(max_length=256, verbose_name='商品详细名称')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='最近编辑时间')
    type = models.CharField(max_length=16, choices=ProductTypeChoices.choices, verbose_name='商品类型')
    # producer = models.ForeignKey(Producer, verbose_name='生产者')
    is_active = models.BooleanField(default=True, verbose_name='是否可用')
    is_gift = models.BooleanField(default=False, verbose_name='是否为赠品')
    # 两位小数，最大值为99,999,999.99。
    # Note: 可使用django-money(https://github.com/django-money/django-money)升级。
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='价格')

    class Meta:
        verbose_name = '商品'
        ordering = ['updated_at']


# class GoodsProfile(models.Model):
#     """
#     实物商品Profile
#     """
#     pass
#
#
# class ServicesProfile(models.Model):
#     """
#     服务（即虚拟商品）
#     """
#     pass
#
#
# class BundleProfile(models.Model):
#     """
#     商品组合
#     """
#     pass
#
#
# class BundleItem(models.Model):
#     """
#     商品组合单元
#     """
#     id = models.UUIDField()
#     bundle = models.ForeignKey(BundleProfile, related_name='items')
