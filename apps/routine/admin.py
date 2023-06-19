from django.contrib import admin

from apps.routine.models import Routine


class RoutineAdminConfig(admin.ModelAdmin):
    model = Routine

    # Campos de escritura
    fields = (
        'name',
        'group',
    )

    # Campos que se muestran (todos)
    list_display = (
        'id',
        'name',
        'group',
        'created_at',
        'updated_at',
    )


admin.site.register(Routine, RoutineAdminConfig)
