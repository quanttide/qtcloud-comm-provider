import uuid

from django.db import models
from djmoney.models.fields import MoneyField


class WalletTypeChoices(models.TextChoices):
    """
    钱包类型

    TODO: 进一步规范字段命名
    """
    individual = 'individual', '个人'
    enterprise = 'enterprise', '企业'


class Wallet(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, verbose_name='钱包ID')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='钱包创建时间')
    type = models.CharField(max_length=16, choices=WalletTypeChoices.choices, verbose_name='钱包类型')

    class Meta:
        verbose_name = '钱包'


class Balance(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    wallet = models.ForeignKey(Wallet, related_name='balances', on_delete=models.CASCADE, verbose_name='关联钱包')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 金融级标准
    # https://stackoverflow.com/questions/224462/storing-money-in-a-decimal-column-what-precision-and-scale/224866#224866
    balance = MoneyField(max_digits=19, decimal_places=4, default_currency='CNY', verbose_name='余额')

    class Meta:
        verbose_name = '余额'


class IndividualProfile(models.Model):
    """
    TODO: 限制type=individual
    """
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    wallet = models.OneToOneField(Wallet, on_delete=models.CASCADE, verbose_name='关联钱包')

    class Meta:
        verbose_name = '个人账户'


class EnterpriseProfile(models.Model):
    """
    TODO: 限制type=enterpise
    """
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    wallet = models.OneToOneField(Wallet, on_delete=models.CASCADE, verbose_name='关联钱包')

    class Meta:
        verbose_name = '企业账户'
