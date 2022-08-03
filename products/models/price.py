import uuid

from django.db import models
import reversion

from .product import Product


# @reversion.register()
# class Price(models.Model):
#     """
#     价格
#
#
#     TODO:
#      - 对数据表做版本管理
#      - 确认是否需要更准确的表达金融数据的字段
#     """
#     id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
#     # 关联Goods或者Service或者Bundle
#     product = models.ForeignKey(Product, related_name='price', on_delete=models.CASCADE, verbose_name='课程')
#     # 商品
#     price = models.DoubleField()
