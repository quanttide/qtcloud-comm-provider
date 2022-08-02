# -*- coding: utf-8 -*-

from django.db import models


class Bundle(models.Model):
    """
    商品组合
    """
    id = models.UUIDField()
