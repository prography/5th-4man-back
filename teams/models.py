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
    image = models.ImageField('이미지', upload_to="team/image/%Y/%m/%d/", default='default.png')
    objective = models.CharField('목적', max_length=1, blank=True)
    likes = models.ManyToManyField(User, related_name='like_teams', verbose_name="좋아요")
    end_date = models.DateTimeField('마감일')
    description = models.TextField('세부 설명')
    max_personnel = models.PositiveSmallIntegerField('최대 인원')
    current_personnel = models.PositiveSmallIntegerField('현재 인원', default=0)
    created_at = models.DateTimeField('생성 시각', auto_now_add=True)
    updated_at = models.DateTimeField('수정 시각', auto_now=True)

    @property
    def like_count(self):
        return self.likes.count()


class BookMark(models.Model):
    pass
