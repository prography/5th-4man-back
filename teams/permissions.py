from rest_framework import permissions


class IsLeaderOrReadCreateOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ('GET', 'HEAD', 'OPTIONS', 'POST',):
            return True
        elif request.method in ('PUT', 'PATCH', 'DELETE',):
            return obj.leader == request.user


class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsLeader(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.leader == request.user
