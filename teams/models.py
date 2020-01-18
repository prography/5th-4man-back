from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    STATUS_WAITING, STATUS_EXPIRY, STATUS_COMPLETE = "waiting", "expiry", "complete"
    STATUS_CHOICES = (
        (STATUS_WAITING, '대기중'),
        (STATUS_EXPIRY, '만료됨'),
        (STATUS_COMPLETE, '완됨'),
    )
    leader = models.ForeignKey(User, related_name='teams', verbose_name='리더', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='teams', verbose_name='태그', blank=True)
    title = models.CharField('제목', max_length=20)
    image = models.ImageField('이미지', upload_to="team/image/%Y/%m/%d/", default='default.png')
    objective = models.CharField('목적', max_length=1, blank=True)
    likes = models.ManyToManyField(User, related_name='like_teams', verbose_name="좋아요")
    end_date = models.DateTimeField('마감일')
    description = models.TextField('세부 설명')
    max_personnel = models.PositiveSmallIntegerField('최대 인원')
    created_at = models.DateTimeField('생성 시각', auto_now_add=True)
    updated_at = models.DateTimeField('수정 시각', auto_now=True)
    status = models.CharField('상태', max_length=10, choices=STATUS_CHOICES, default=STATUS_WAITING)

    @property
    def like_count(self):
        like_count = getattr(self, '__like_count', self.likes.count())
        return like_count

    # Todo: DB 최적화 확인하기. annotate, select(prefetch) related ...
    @property
    def current_personnel(self):
        current_personnel = self.applications.count()
        return current_personnel

    @like_count.setter
    def like_count(self, count):
        self.__like_count = count


class Comment(models.Model):
    parent = models.ForeignKey("self", verbose_name='부모 댓글', related_name='child_comments', on_delete=models.CASCADE,
                               blank=True, null=True)
    team = models.ForeignKey(Team, verbose_name='팀', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name='작성자', related_name='comments', on_delete=models.CASCADE)
    body = models.CharField('본문', max_length=300)
    created_at = models.DateTimeField('생성 시각', auto_now_add=True)
    updated_at = models.DateTimeField('수정 시각', auto_now=True)

    class Meta:
        ordering = ['created_at']
