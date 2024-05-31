from .permissions import CustomPermission


class CustomPermissionMixin():
    permission_classes = [CustomPermission]