from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from rest_framework.decorators import action


class WalletView(GenericAPIView, mixins.RetrieveModelMixin):
    @action(methods=['POST'], url_path='add-balance')
    def add_balance(self):
        """
        TODO: 另外一种设计思路是PATCH，修改balance字段。
        :return:
        """
        pass
