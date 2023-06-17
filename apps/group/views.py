from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.group.models import Group
from apps.group.serializers import GroupSerializer
from apps.group.doc_decorators import doc_view_group_list, doc_view_group_retrieve, doc_view_group_create, \
    doc_view_group_partial_update, doc_view_group_destroy


class GroupView(viewsets.ModelViewSet):
    """
    View de Group
    """
    queryset = Group.objects.all()

    serializer_class = GroupSerializer

    permission_classes = (IsAuthenticated, )

    filterset_fields = {
        'name': ['exact'],
    }

    search_fields = {
        'name',
    }

    ordering_fields = ['created_at', 'updated_at']

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return self.queryset
        else:
            return Group.objects.filter(users_list=user)

    @doc_view_group_list
    def list(self, request, *args, **kwargs):
        """
        Listar Groups.

        Petición para listar Grupos.
        """
        result = super().list(request, *args, **kwargs)
        return result

    @doc_view_group_retrieve
    def retrieve(self, request, *args, **kwargs):
        """
        Obtener un Group.

        Petición para obtener un Group.
        """
        result = super().retrieve(request, *args, **kwargs)
        return result

    @doc_view_group_create
    def create(self, request, *args, **kwargs):
        """
        Crear Group.

        Petición para crear Group.
        """
        result = super().create(request, *args, **kwargs)
        return result

    # @doc_view_group_partial_update
    def partial_update(self, request, *args, **kwargs):
        """
        Actualizar parcialmente Group

        Petición para actualizar parcialmente un Group.
        """
        result = super().partial_update(request, *args, **kwargs)
        return result

    # @doc_view_group_destroy
    def destroy(self, request, *args, **kwargs):
        """
        Eliminar Group.

        Petición para eliminar Group.
        """
        result = super().destroy(request, *args, **kwargs)
        return result
