from django.db import models


class Price(models.Model):
    """
    价格
    """
    id = models.UUIDField()
    # 关联Goods或者Service或者Bundle
    product_id = models.UUIDField()
