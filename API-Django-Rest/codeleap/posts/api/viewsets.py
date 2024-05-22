from rest_framework import viewsets
from posts import models
from posts.api import serializers

class PostsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PostsSerializer
    queryset = models.Posts.objects.all()