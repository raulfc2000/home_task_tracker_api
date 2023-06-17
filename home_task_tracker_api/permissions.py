from rest_framework import permissions


class IsSuperUser(permissions.BasePermission):
    """
    Permiso custom para identificar que es superusuario.
    """
    def has_permission(self, request, view):
        user = request.user
        if user and user.is_authenticated:
            return user.is_superuser


class UserInGroup(permissions.BasePermission):
    """
    Permiso custom para identificar que el user está en el Group que se está accediendo
    """
    def has_permission(self, request, view):
        return False


class IsMemberOfGroup(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user and user.is_authenticated:
            return user in obj.users_list.all()
