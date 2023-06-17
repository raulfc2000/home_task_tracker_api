from rest_framework import permissions


class IsSuperUser(permissions.BasePermission):
    """
    Permiso custom para identificar que es superusuario.
    """
    def has_permission(self, request, view):
        # User
        user = request.user

        # Si existe el usuario y está autenticado, es superusuario
        if user and user.is_authenticated:
            return user.is_superuser
