from django.db import models


class Product(models.Model):
    """
    商品/产品
    """
    id = models.UUIDField()
    is_active = models.BooleanField()
