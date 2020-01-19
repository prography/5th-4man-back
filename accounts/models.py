from django.db import models
from django.contrib.auth.models import AbstractUser


class GithubProfile(models.Model):
    login = models.CharField('깃허브 로그인 아이디', max_length=50)
    avatar = models.URLField('아바타')
    email = models.EmailField('이메일', blank=True, null=True)
    languages = models.TextField('언어', blank=True)

    def __str__(self):
        return self.login


class User(AbstractUser):
    profile = models.OneToOneField(GithubProfile, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='user', verbose_name='프로필')
    nickname = models.CharField('별명', max_length=10, blank=True)
    introduction = models.CharField('한 줄 소개', max_length=100, blank=True)
    upload_image = models.ImageField('프로필 사진', upload_to="user_image/profile/%Y/%m/%d/", blank=True,
                                     default='default_user_image.png')

    @property
    def is_github_authenticated(self):
        return self.profile_id is not None

    @property
    def image(self):
        if self.upload_image.name != "default_user_image.png":
            return self.upload_image.url
        elif self.profile_id is not None:
            return self.profile.avatar
        return self.upload_image.url
