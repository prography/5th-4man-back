from django.db import models
from django.contrib.auth import get_user_model
from teams.models import Team

User = get_user_model()


class Application(models.Model):
    team = models.ForeignKey(Team, verbose_name='팀', related_name='applications', on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, verbose_name='지원자', related_name='applications', on_delete=models.CASCADE)
    reason = models.TextField('지원 동기', max_length=200)
    github_account = models.CharField('깃허브 계정', max_length=20)
    created_at = models.DateTimeField('생성 시각', auto_now_add=True)
    updated_at = models.DateTimeField('수정 시각', auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['team', 'applicant'], name='unique_application'),
        ]
