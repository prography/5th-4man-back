from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Team

User = get_user_model()
'''
    leader = models.ForeignKey(User, related_name='teams', verbose_name='리더', on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill, related_name='teams', verbose_name='기술')
    title = models.CharField('제목', max_length=20)
    objective = models.CharField('목적', max_length=1)
    recruit_count = models.PositiveSmallIntegerField('모집 인원')
    recruit = models.ManyToManyField(User)
    end_date = models.DateTimeField('마감일')
    description = models.TextField('세부 설명')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
'''


class TeammateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'nickname')


class TeamSerializer(serializers.ModelSerializer):
    leader = TeammateSerializer(read_only=True)

    class Meta:
        model = Team
        fields = ('id', 'leader', 'title', 'objective', 'end_date', 'description', 'created_at', 'updated_at')

    def create(self, validated_data):
        user = self.context.get("request").user
        validated_data["leader"] = user
        request = super().create(validated_data)
        return request
