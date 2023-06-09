from django.urls import path, include
from rest_framework import routers
from .views import AccountViewSet

router = routers.DefaultRouter()
router.register(r'', AccountViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
