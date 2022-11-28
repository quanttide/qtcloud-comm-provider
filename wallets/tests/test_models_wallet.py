from django_tenants.test.cases import TenantTestCase


class WalletTestCase(TenantTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        super(TenantTestCase, cls).setUpClass()

    def test_add_balance(self):
        pass
