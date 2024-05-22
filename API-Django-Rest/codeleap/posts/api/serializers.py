from rest_framework import serializers
from posts import models

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Posts
        fields = '__all__'