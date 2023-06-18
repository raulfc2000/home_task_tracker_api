from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.routine.doc_decorators import doc_view_routine_list, doc_view_routine_retrieve, doc_view_routine_create, \
    doc_view_routine_partial_update, doc_view_routine_destroy
from apps.routine.models import Routine
from apps.routine.serializers import RoutineSerializer


class RoutineView(viewsets.ModelViewSet):
    """
    View de Routine
    """
    queryset = Routine.objects.all()

    serializer_class = RoutineSerializer

    permission_classes = (IsAuthenticated, )

    filterset_fields = {
        'name': ['exact'],
        'group': ['exact'],
    }

    search_fields = {
        'name',
    }

    ordering_fields = ['created_at', 'updated_at']

    def get_queryset(self):
        """
        Modificación del queryset
        """
        user = self.request.user

        # Si es superuser recibirá el queryset genérico
        if user.is_superuser:
            return self.queryset
        # Si no lo es, filtrará por los grupos a los que pertenezca.
        else:
            return Routine.objects.filter(group__users_list=user.id)

    @doc_view_routine_list
    def list(self, request, *args, **kwargs):
        """
        Listar Routines.

        Petición para listar Rutinas.
        """
        result = super().list(request, *args, **kwargs)
        return result

    @doc_view_routine_retrieve
    def retrieve(self, request, *args, **kwargs):
        """
        Obtener un Routine.

        Petición para obtener un Routine.
        """
        result = super().retrieve(request, *args, **kwargs)
        return result

    @doc_view_routine_create
    def create(self, request, *args, **kwargs):
        """
        Crear Routine.

        Petición para crear Routine.
        """
        result = super().create(request, *args, **kwargs)
        return result

    @doc_view_routine_partial_update
    def partial_update(self, request, *args, **kwargs):
        """
        Actualizar parcialmente Routine

        Petición para actualizar parcialmente un Routine.
        """
        result = super().partial_update(request, *args, **kwargs)
        return result

    @doc_view_routine_destroy
    def destroy(self, request, *args, **kwargs):
        """
        Eliminar Routine.

        Petición para eliminar Routine.
        """
        result = super().destroy(request, *args, **kwargs)
        return result
