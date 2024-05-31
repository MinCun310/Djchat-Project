from rest_framework.permissions import BasePermission


class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_staff:
            return True
        return False
