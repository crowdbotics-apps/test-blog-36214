from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import LikeViewSet

router = DefaultRouter()
router.register("like", LikeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
