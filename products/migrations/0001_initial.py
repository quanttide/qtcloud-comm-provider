# Generated by Django 4.1.3 on 2022-11-28 16:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Producer",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="生产者ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=128, unique=True, verbose_name="生产者名称"),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("goods_producer", "实物商品制造商"),
                            ("service_provider", "服务提供者"),
                        ],
                        max_length=16,
                        verbose_name="生产者类型",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="商品ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=128, unique=True, verbose_name="商品名称"),
                ),
                (
                    "verbose_name",
                    models.CharField(max_length=256, verbose_name="商品详细名称"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="最近编辑时间"),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("goods", "实物商品"),
                            ("service", "服务"),
                            ("bundle", "商品组合"),
                        ],
                        max_length=16,
                        verbose_name="商品类型",
                    ),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="是否可用")),
                ("is_gift", models.BooleanField(default=False, verbose_name="是否为赠品")),
                (
                    "producer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="producer",
                        to="products.producer",
                        verbose_name="生产者",
                    ),
                ),
            ],
            options={
                "verbose_name": "商品",
                "ordering": ["updated_at"],
            },
        ),
        migrations.CreateModel(
            name="Price",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="价格"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="price_models",
                        to="products.product",
                        verbose_name="课程",
                    ),
                ),
            ],
            options={
                "verbose_name": "价格",
                "ordering": ["created_at"],
                "get_latest_by": "created_at",
            },
        ),
    ]
