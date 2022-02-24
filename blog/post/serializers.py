from .models import Post, Comment
from rest_framework.serializers import ModelSerializer, ReadOnlyField


class CommentSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.name')
    post_id = ReadOnlyField(source='post.id')

    class Meta:
        model = Comment
        fields = ['id', 'post_id', 'content', 'author']


class PostSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.name')

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'author')



