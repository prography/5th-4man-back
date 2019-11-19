from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Team, Tag
from .serializers import TeamSerializer, TagSerializer
from .permissions import IsLeaderOrReadCreateOnly


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = super().get_queryset()
        key = self.request.query_params.get('search', None)
        if key is not None:
            queryset = queryset.filter(name__startswith=key)
        return queryset


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsLeaderOrReadCreateOnly,)

    def perform_create(self, serializer):
        serializer.save(leader=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == 'recent':
            queryset = queryset[:12]
        return queryset

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
