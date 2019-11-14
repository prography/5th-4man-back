from django.db import models
from django.contrib.auth.models import AbstractUser


class GithubProfile(models.Model):
    login = models.CharField('깃허브 로그인 아이디', max_length=50)
    avatar = models.URLField('아바타')
    email = models.EmailField('이메일', blank=True, null=True)
    languages = models.TextField('언어', blank=True)


class User(AbstractUser):
    profile = models.OneToOneField(GithubProfile, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='user', verbose_name='프로필')
    nickname = models.CharField('별명', max_length=10, blank=True)
    image = models.ImageField('프로필 사진', upload_to="user_image/profile/%Y/%m/%d/", blank=True)
