from rest_framework import permissions


class IsTeamLeader(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.team.leader == request.user
