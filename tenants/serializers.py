from rest_framework import serializers

from tenants.models import Tenant


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        depth = 1
        fields = '__all__'

    def create(self, validated_data):
        """
        创建租户，同时创建租户域名和系统管理员。

        :param validated_data:
        :return:
        """
        return super().create(validated_data)
