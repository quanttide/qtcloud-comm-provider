from django.db import models


class OrderStatusChoices(models.TextChoices):
    """
    订单状态
    """
    pass


class Order(models.Model):
    """
    订单数据模型
    """
    id = models.UUIDField()
    status = models.CharField(max_length=16)
    product_id = models.UUIDField()

