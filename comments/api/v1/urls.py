from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import CommentViewSet

router = DefaultRouter()
router.register("comment", CommentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
