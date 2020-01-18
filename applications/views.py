from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Application
from .serializers import ApplicationSerializer
from .permissions import IsTeamLeader


class ApplicationViewSet(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = (IsAuthenticated,)

    def _change_application_status(self, request, status, pk=None):
        team = self.get_object()
        team.status = status
        team.save()
        serializer = self.get_serializer()
        return Response(serializer(team))

    @action(methods=["post"], detail=True, permission_classes=[IsAuthenticated, IsTeamLeader], url_path="refuse")
    def refuse_application(self, request, pk=None):
        return self._change_application_status(request, 'refuse', pk)

    @action(methods=["post"], detail=True, permission_classes=[IsAuthenticated, IsTeamLeader], url_path="approve")
    def approve_application(self, request, pk=None):
        return self._change_application_status(request, 'approved', pkq)
