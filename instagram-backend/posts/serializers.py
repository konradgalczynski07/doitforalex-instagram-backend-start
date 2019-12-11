from django.contrib.auth import get_user_model
from rest_framework import serializers
from posts.models import Post, Comment
User = get_user_model()


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'profile_pic')


class CommentSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'text', 'posted_on')
        read_only_fields = ('author', 'id', 'posted_on')


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    post_comments = CommentSerializer(read_only=True, many=True)
    photo = serializers.ImageField(max_length=None, allow_empty_file=False)
    liked_by_req_user = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id',
            'author',
            'photo',
            'text',
            'location',
            'posted_on',
            'number_of_likes',
            'liked_by_req_user',
            'post_comments',
        )

    def get_liked_by_req_user(self, obj):
        user = self.context['request'].user
        return user in obj.likes.all()
