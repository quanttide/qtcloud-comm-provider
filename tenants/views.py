"""

"""

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from tenants.models import Tenant
from tenants.serializers import TenantSerializer
from tenants.authentication import QtCloudIdAMAdminAuthentication


class TenantViewSet(ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    lookup_field = 'schema_name'  # TODO: `name`
    authentication_classes = [QtCloudIdAMAdminAuthentication]
    permission_classes = [IsAuthenticated]
