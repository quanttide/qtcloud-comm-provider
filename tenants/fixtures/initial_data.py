from dynamic_initial_data.base import BaseInitialData

from tenants.models import Tenant, TenantDomain


class InitialData(BaseInitialData):
    dependencies = []

    def update_initial_data(self):
        """
        创建初始租户及域名，同时自动创建租户schema。
        """
        tenant, tenant_created = Tenant.objects.get_or_create(schema_name='quanttide', verbose_name='量潮科技')
        # TODO: change domain value to default value
        domain, domain_created = TenantDomain.objects.get_or_create(tenant=tenant, domain='quanttide.qtcloud-payments.quanttideapi.com', is_primary=True)
