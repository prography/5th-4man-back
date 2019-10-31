from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickname = models.CharField(max_length=10)
    image = models.ImageField(upload_to="user_image/profile/%Y/%m/%d/", blank=True)


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     skill = models.ManyToManyField(Skill, related_name='profiles')


# class SocialUser(models.Model):
#     user = models.ForeignKey()
