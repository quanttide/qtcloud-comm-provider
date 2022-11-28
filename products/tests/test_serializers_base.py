from django_tenants.test.cases import TenantTestCase as TestCase

from products.models.product import Price
from products.serializers.base import ProductSerializer


class ProductSerializerTestCase(TestCase):
    fixtures = ['services.json']
    serializer_class = ProductSerializer
    model_class = serializer_class.Meta.model

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        super(TestCase, cls).setUpClass()

    def setUp(self):
        self.product = self.model_class.objects.get(name='python')

    def test_serialize(self):
        serializer = ProductSerializer(self.product)
        self.assertEqual('python', serializer.data['name'])
        self.assertEqual(0.2, float(serializer.data['price']))

    def test_create(self):
        data = {'name': 'django', 'verbose_name': 'Django教程',
                'type': 'service', 'price': 0.1,
                'producer': {'name': 'qtclass'}}
        serializer = ProductSerializer(data=data)
        self.assertTrue(serializer.is_valid(raise_exception=True))
        serializer.save()
        # 验证Product模型
        self.assertEqual('django', serializer.instance.name)
        # 验证Producer模型
        self.assertEqual('qtclass', serializer.instance.producer.name)
        # 验证Price模型
        price = Price.objects.filter(product=serializer.instance).latest().price
        self.assertEqual(0.1, float(price))

    def test_update(self):
        # 上次更新
        latest_updated = self.product.updated_at
        # 待更新的数据
        data = {'name': 'python', 'verbose_name': 'Python编程课程', 'price': 0.3}
        # 反序列化
        serializer = ProductSerializer(instance=self.product, data=data, partial=True)
        self.assertTrue(serializer.is_valid())
        # 验证，validated_data只有data的几个字段
        self.assertEqual(0.3, float(serializer.validated_data['price']))
        # 更新
        serializer.save()
        # 验证verbose_name更新
        self.assertEqual(data['verbose_name'], self.product.verbose_name)
        # 验证时间更新
        self.assertTrue(latest_updated < self.product.updated_at)
        # 验证价格更新
        price = Price.objects.filter(product=serializer.instance).latest().price
        self.assertEqual(0.3, float(price))

    def test_delete(self):
        serializer = ProductSerializer(instance=self.product)
        serializer.delete()
        self.assertFalse(self.product.is_active)
