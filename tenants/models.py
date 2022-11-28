"""
租户及域名模型
"""

import uuid

from django.db import models
from django.conf import settings
from django_tenants.models import TenantMixin as BaseTenant, DomainMixin as BaseTenantDomain
from django_tenants.postgresql_backend.base import _check_schema_name


class TenantManager(models.Manager):
    def get(self, **kwargs):
        """
        TODO: 定义使用name查询的逻辑，方便符合量潮Django手册对name字段的定义。
        :param kwargs:
        :return:
        """
        return super().get(**kwargs)


class Tenant(BaseTenant):
    """
    租户

    通过`id`或`schema_name`字段查询

    CHANGELOG:
      - v0.1.0: 增加`id`, `schema_name`, `verbose_name`, `created_at`, `updated_at`字段。
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='租户ID')
    schema_name = models.CharField(max_length=63, unique=True, db_index=True,
                                   validators=[_check_schema_name], verbose_name='租户标识')
    verbose_name = models.CharField(max_length=256, verbose_name='租户名称')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='租户创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='租户修改时间')

    class Meta:
        verbose_name = '租户'

    @property
    def name(self):
        return self.schema_name


class TenantDomain(BaseTenantDomain):
    """
    租户域名

    CHANGELOG:
      - v0.1.0: 增加`domain`, `tenant`, `is_primary`字段。
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='租户域名ID')
    tenant = models.ForeignKey(settings.TENANT_MODEL, db_index=True, related_name='domains',
                               on_delete=models.CASCADE, verbose_name='关联租户')
    # TODO: 定义默认值
    domain = models.CharField(max_length=253, unique=True, db_index=True, verbose_name='租户域名')
    # Set this to true if this is the primary domain
    is_primary = models.BooleanField(default=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='租户域名创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='租户域名修改时间')

    class Meta:
        verbose_name = '租户域名'
