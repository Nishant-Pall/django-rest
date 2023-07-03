from unittest.mock import Base
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of object to edit it
    """

    def has_object_permission(self, request, view, obj):
        # Allow read permissions to everyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet
        return obj.owner == request.user
