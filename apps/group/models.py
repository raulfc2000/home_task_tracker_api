from django.contrib.auth.models import User
from django.db import models


class Group(models.Model):
    """
    Modelo Group
    - id: (IntegerField) Número entero, único y auto-incremental, asignado automáticamente.
    - name: (CharField) String, nombre del grupo.
    - user_owner: (OneToOneField) Usuario que ha creado el group. Se asignará automáticamente.
    - users_list: (ManyToManyField) Listado de usuarios que pertenecen al grupo. Se usará para los permisos.
    - routine: (ReverseOneToOneField) OneToOneField que vendrá desde la rutina asociada al grupo.

    - created_at: (DateTimeField) Fecha en la cual se creó el grupo.
    - updated_at: (DateTimeField) Fecha de la última actualización realizada al grupo.
    """
    name = models.CharField(verbose_name='Nombre del grupo', max_length=120)
    user_owner = models.OneToOneField(User,
                                      verbose_name='Usuario propietario',
                                      on_delete=models.CASCADE,
                                      related_name='owner_of_group')
    users_list = models.ManyToManyField(User, verbose_name='Listado de usuarios', related_name='user_in_groups')
