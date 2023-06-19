from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.task.doc_decorators import doc_view_task_list, doc_view_task_retrieve, doc_view_task_create, \
    doc_view_task_partial_update, doc_view_task_destroy
from apps.task.models import Task
from apps.task.serializers import TaskSerializer


class TaskView(viewsets.ModelViewSet):
    """
    View de Task
    """
    queryset = Task.objects.all()

    serializer_class = TaskSerializer

    permission_classes = (IsAuthenticated, )

    filterset_fields = {
        'routine': ['exact'],
        'starts_at': ['gte'],
        'created_by': ['exact'],
        'assigned_to': ['exact'],
        'completed': ['exact'],
    }

    search_fields = {
        'title',
        'description',
    }

    ordering_fields = ['created_at', 'updated_at', 'starts_at']

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
            return Task.objects.filter(routine__group__users_list=user.id)

    @doc_view_task_list
    def list(self, request, *args, **kwargs):
        """
        Listar Tasks.

        Petición para listar Tareas.
        """
        result = super().list(request, *args, **kwargs)
        return result

    @doc_view_task_retrieve
    def retrieve(self, request, *args, **kwargs):
        """
        Obtener un Task.

        Petición para obtener un Task.
        """
        result = super().retrieve(request, *args, **kwargs)
        return result

    @doc_view_task_create
    def create(self, request, *args, **kwargs):
        """
        Crear Task.

        Petición para crear Task.
        """
        result = super().create(request, *args, **kwargs)
        return result

    @doc_view_task_partial_update
    def partial_update(self, request, *args, **kwargs):
        """
        Actualizar parcialmente Task

        Petición para actualizar parcialmente un Task.
        """
        result = super().partial_update(request, *args, **kwargs)
        return result

    @doc_view_task_destroy
    def destroy(self, request, *args, **kwargs):
        """
        Eliminar Task.

        Petición para eliminar Task.
        """
        result = super().destroy(request, *args, **kwargs)
        return result
