from rest_framework import routers
from django.contrib import admin
from django.urls import path
from cielo.api.viewsets import CompraViewSet
from cielo.api.viewsets import HoodidViewSet
from django.conf.urls import include


router = routers.SimpleRouter()
router.register(r'api/cartao', CompraViewSet)
router.register(r'api/hoodid', HoodidViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),


]
