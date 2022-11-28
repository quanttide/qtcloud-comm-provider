from rest_framework.routers import SimpleRouter

from tenants.views import TenantViewSet


router = SimpleRouter()
router.register(prefix='tenants', viewset=TenantViewSet, basename='tenant')
urlpatterns = router.urls
