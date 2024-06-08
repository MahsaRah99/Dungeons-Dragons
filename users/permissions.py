from rest_framework.permissions import BasePermission


class PrimaryPermission(BasePermission):
    message = "Not Authenticated"

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated


class IsCharacterOwner(PrimaryPermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
