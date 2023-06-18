from django.db import models

from apps.group.models import Group


class Routine(models.Model):
    """
    Modelo Routine
    - id: (IntegerField) Número entero, único y auto-incremental, asignado automáticamente.
    - group: (ForeignKey) Grupo al que pertenece la rutina.

    - created_at: (DateTimeField) Fecha en la cual se creó el grupo.
    - updated_at: (DateTimeField) Fecha de la última actualización realizada al grupo.
    """
    name = models.CharField(verbose_name='Nombre de la rutina', max_length=120)
    group = models.ForeignKey(Group, verbose_name='Grupo', on_delete=models.CASCADE, related_name='routines')

    created_at = models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha de actualización', auto_now=True)

    class Meta:
        unique_together = ('name', 'group')
