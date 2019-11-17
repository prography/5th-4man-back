from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.decorators import action
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
        skill = self.request.query_params.get('', None)
        if self.action == 'recent':
            queryset = queryset[:12]
        if skill is not None:
            queryset = queryset.filter()
        return queryset

    @action(methods=["get"], detail=False)
    def recent(self, request, *args, **kwargs):
        return self.list(request)
