from django.contrib import admin

from apps.task.models import Task


class TaskAdminConfig(admin.ModelAdmin):
    model = Task

    # Campos de escritura
    fields = (
        'routine',
        'title',
        'description',
        'starts_at',
        'created_by',
        'assigned_to',
        'completed',
    )

    # Campos de búsqueda (en la view)
    search_fields = (
        'title',
        'description',
    )

    # Campos de filtro (en la view)
    list_filter = (
        'routine',
        'starts_at',
        'created_by',
        'assigned_to',
        'completed',
    )

    # Campos que se muestran (todos)
    list_display = (
        'id',
        'routine',
        'title',
        'description',
        'starts_at',
        'created_by',
        'assigned_to',
        'completed',
        'created_at',
        'updated_at',
    )

    # Sobreescribir el form para que el campo de users_list no sea obligatorio
    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super(TaskAdminConfig, self).get_form(request, obj, **kwargs)
        form.base_fields['description'].required = False
        form.base_fields['created_by'].required = False
        form.base_fields['assigned_to'].required = False
        return form


admin.site.register(Task, TaskAdminConfig)
