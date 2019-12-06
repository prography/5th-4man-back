from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Team, Tag, Comment

User = get_user_model()


class TeammateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'nickname', 'image')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


class ChildCommentSerializer(serializers.ModelSerializer):
    author = TeammateSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'parent', 'team', 'author', 'body', 'created_at', 'updated_at']


class CommentSerializer(ChildCommentSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['child_comments'] = self.__class__.__base__(many=True, read_only=True)
        self.Meta.fields.append('child_comments')


class TeamSerializer(serializers.ModelSerializer):
    leader = TeammateSerializer(read_only=True)
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all(), pk_field=serializers.CharField())
    likes = TeammateSerializer(read_only=True, many=True)
    image = serializers.ImageField(required=False, use_url=True)
    parent_comments = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = (
            'id', 'tags', 'likes', 'like_count', 'leader', 'title', 'end_date', 'description', 'image', 'max_personnel',
            'current_personnel', 'parent_comments', 'created_at', 'updated_at')

    def get_parent_comments(self, obj):
        parent_comments = obj.comments.filter(parent=None)
        serializer = CommentSerializer(parent_comments, many=True)
        return serializer.data
