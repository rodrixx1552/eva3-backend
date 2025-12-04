from django.urls import path, include
from rest_framework import routers
from .views import ProductoViewSet

router = routers.DefaultRouter()
router.register('productos', ProductoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]