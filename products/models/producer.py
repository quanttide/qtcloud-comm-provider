# -*- coding: utf-8 -*-

from django.db import models


# class ProducerTypeChoices(models.Model):
#     goods_producer = 'goods_producer', '实物商品制造商'
#     service_provider = 'service_provider', '服务提供者'
#
#
# class Producer(models.Model):
#     id = models.UUIDField()
#     name = models.CharField(max_length=64, unique=True)
#     type = models.CharField(max_length=8, choices=ProducerTypeChoices.choices)
#
#
# class GoodsProducerProfile(models.Model):
#     """
#     实物商品生产者Profile
#     """
#     id = models.UUIDField()
#     producer = models.ForeignKey(Producer)
#
#
# class ServiceProviderProfile(models.Model):
#     """
#     服务提供者Profile
#     """
#     pass
