from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Recruit(models.Model):
    pass


class Application(models.Model):
    pass


class Tag(models.Model):
    name = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    leader = models.ForeignKey(User, related_name='teams', verbose_name='리더', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='teams', verbose_name='태그')
    title = models.CharField('제목', max_length=20)
    objective = models.CharField('목적', max_length=1, blank=True)
    likes = models.ManyToManyField(User, related_name='like_teams', verbose_name="좋아요")
    end_date = models.DateTimeField('마감일')
    description = models.TextField('세부 설명')
    created_at = models.DateTimeField('생성 시각', auto_now_add=True)
    updated_at = models.DateTimeField('수정 시각', auto_now=True)


class BookMark(models.Model):
    pass
