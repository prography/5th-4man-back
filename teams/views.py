from django.db.models import Count
from django.contrib.auth import get_user_model
from rest_framework import filters, status, mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Team, Tag, Comment
from .serializers import TeamSerializer, TagSerializer, CommentSerializer
from .permissions import IsLeaderOrReadCreateOnly, IsAuthor

User = get_user_model()


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (AllowAny,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class CommentViewSet(mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # TODO: 테스트 끝나면 고쳐야 하는 부분
    # permission_classes = (IsAuthenticated, IsAuthor)
    #
    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)

    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        serializer.save(author=User.objects.get(username='admin'))


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        team = serializer.instance.team
        comment_queryset = team.comments.filter(parent=None)
        data = self.get_serializer(comment_queryset, many=True).data
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsLeaderOrReadCreateOnly)
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('created_at', 'like_count')
    ordering = ('created_at',)

    def filter_queryset(self, queryset):
        queryset = queryset.annotate(like_count=Count('likes'))
        return super().filter_queryset(queryset)

    def perform_create(self, serializer):
        serializer.save(leader=self.request.user)

    @action(methods=["get"], detail=False)
    def recent(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @action(methods=["get"], detail=True, name="Like Team")
    def like(self, request, pk=None):
        user = request.user
        team = self.get_object()

        if user in team.likes.all():
            team.likes.remove(user)
        else:
            team.likes.add(user)
        return Response(TeamSerializer(team).data)
