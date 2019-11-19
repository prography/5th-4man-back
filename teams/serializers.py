from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Team, Tag

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'nickname')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


class TeamSerializer(serializers.ModelSerializer):
    leader = UserSerializer(read_only=True)
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all(), pk_field=serializers.CharField())
    likes = UserSerializer(read_only=True, many=True)
    image = serializers.ImageField(required=False, use_url=True)

    class Meta:
        model = Team
        fields = (
            'id', 'tags', 'likes', 'like_count', 'leader', 'title', 'end_date', 'description', 'image', 'created_at',
            'updated_at')
