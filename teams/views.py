from django.db.models import Count
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Team, Tag, Comment
from .serializers import TeamSerializer, TagSerializer, CommentSerializer
from .permissions import IsLeaderOrReadCreateOnly, IsAuthor


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
    permission_classes = (IsAuthenticated, IsAuthor)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


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
