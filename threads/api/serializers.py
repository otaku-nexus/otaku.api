from rest_framework import serializers
from threads.models import Thread, Post, Like

class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = ['id', 'title', 'creator', 'created_at', 'updated_at']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'post', 'user', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    # comments = CommentSerializer(many=True, read_only=True)
    likes = LikeSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'content', 'author', 'created_at', 'likes']


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True, source='replies')  # Assuming 'replies' is the related name for comments on the Post model
    likes = LikeSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'thread', 'author', 'content', 'parent', 'created_at', 'updated_at', 'comments', 'likes']
        # depth = 3