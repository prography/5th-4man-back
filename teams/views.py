from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Team
from .serializers import TeamSerializer
from .permissions import IsLeaderOrReadCreateOnly


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsLeaderOrReadCreateOnly,)

    def perform_create(self, serializer):
        serializer.save(leader=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        skill = self.request.query_params.get('', None)
        if skill is not None:
            queryset = queryset.filter()
        return queryset
