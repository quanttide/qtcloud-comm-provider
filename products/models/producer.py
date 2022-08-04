# -*- coding: utf-8 -*-
import uuid
from django.db import models


class ProducerTypeChoices(models.TextChoices):
    goods_producer = 'goods_producer', '实物商品制造商'
    service_provider = 'service_provider', '服务提供者'


class Producer(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, verbose_name='生产者ID')
    name = models.CharField(max_length=64, unique=True, verbose_name='生产者名称')
    type = models.CharField(max_length=16, choices=ProducerTypeChoices.choices, verbose_name='生产者类型')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')


# class GoodsProducerProfile(models.Model):
#     """
#     实物商品生产者Profile
#     """
#     id = models.UUIDField()
#     producer = models.ForeignKey(Producer)


# class ServiceProviderProfile(models.Model):
#     """
#     服务提供者Profile
#     """
#     pass
