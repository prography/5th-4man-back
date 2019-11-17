from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Skill(models.Model):
    name = models.CharField(max_length=10, unique=True)


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
    skills = models.ManyToManyField(Skill, related_name='teams', verbose_name='스킬')
    tags = models.ManyToManyField(Tag, related_name='teams', verbose_name='태그')
    title = models.CharField('제목', max_length=20)
    objective = models.CharField('목적', max_length=1)
    recruit = models.ManyToManyField(User)
    end_date = models.DateTimeField('마감일')
    description = models.TextField('세부 설명')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BookMark(models.Model):
    pass
