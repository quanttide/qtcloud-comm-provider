# -*- coding: utf-8 -*-


from rest_framework import routers

from products.views.admin import ProductAdminViewSet


# TODO: drf-admin升级以后，通过Admin应用注册。
router = routers.SimpleRouter()
router.register(r'products', ProductAdminViewSet)
urlpatterns = router.urls
