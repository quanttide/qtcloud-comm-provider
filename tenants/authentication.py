from rest_framework.authentication import BaseAuthentication


class QtCloudIdAMAdminAuthentication(BaseAuthentication):
    """
    租户管理后台令牌鉴权，用Django密钥生成的JWT签名鉴权。
    """
    def authenticate(self, request):
        pass
