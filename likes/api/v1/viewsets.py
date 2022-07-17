from rest_framework import authentication
from likes.models import Like
from .serializers import LikeSerializer
from rest_framework import viewsets


class LikeViewSet(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Like.objects.all()
