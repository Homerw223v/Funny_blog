from ..models import Bloger, Post, Comment
from rest_framework import serializers


# class PostSerializer(serializers.Serializer):     # Решение через serializer.Serializer
#     title = serializers.CharField(max_length=200)
#     post_date = serializers.DateTimeField(read_only=True)
#     description = serializers.CharField()
#     author = serializers.CharField()
#
#     def create(self, validated_data):
#         return Post.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.tilte = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.title)
#         instance.author = validated_data.get('author', instance.title)
#
#     def delete(self, instance):
#         instance.delete()

class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ('title', 'description', 'author')
