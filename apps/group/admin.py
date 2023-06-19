from django.contrib import admin

from apps.group.models import Group


class GroupAdminConfig(admin.ModelAdmin):
    model = Group

    # Campos de escritura
    fields = (
        'name',
        'users_list',
        'user_owner'
    )

    # Campos de búsqueda (en la view)
    search_fields = (
        'name',
    )

    # Campos de filtro (en la view)
    list_filter = (
        'name',
    )

    # Campos que se muestran (todos)
    list_display = (
        'id',
        'name',
        'user_owner',
        'created_at',
        'updated_at',
    )

    # Sobreescribir el form para que el campo de users_list no sea obligatorio
    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super(GroupAdminConfig, self).get_form(request, obj, **kwargs)
        form.base_fields['users_list'].required = False
        return form


admin.site.register(Group, GroupAdminConfig)
