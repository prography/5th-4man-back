from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Team
from .serializers import TeamSerializer
from .permissions import IsLeaderOrReadCreateOnly


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsLeaderOrReadCreateOnly,)

