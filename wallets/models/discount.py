"""
折扣券
"""
import uuid

from django.db import models


class CouponTemplate(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, verbose_name='优惠券模板ID')
    # 关联商品可选
    product = models.ForeignKey('products.Product', default=None, blank=True, null=True, on_delete=models.CASCADE,
                                verbose_name='关联商品')

    class Meta:
        verbose_name = '优惠券模板'


class Coupon(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, verbose_name='优惠券ID')
    template = models.ForeignKey(CouponTemplate, on_delete=models.CASCADE, verbose_name='关联模板')
    wallet = models.ForeignKey('wallets.Wallet', on_delete=models.CASCADE, verbose_name='关联钱包')

    class Meta:
        verbose_name = '优惠券'


class VoucherTemplate(models.Model):
    class Meta:
        verbose_name = '代金券模板'


class Voucher(models.Model):
    class Meta:
        verbose_name = '代金券'



