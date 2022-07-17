from rest_framework import authentication
from comments.models import Comment
from .serializers import CommentSerializer
from rest_framework import viewsets


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Comment.objects.all()
