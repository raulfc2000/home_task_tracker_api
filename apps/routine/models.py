from django.db import models


class Routine(models.Model):
    """
    Modelo Routine
    - id: (IntegerField) Número entero, único y auto-incremental, asignado automáticamente.
    -

    - created_at: (DateTimeField) Fecha en la cual se creó el grupo.
    - updated_at: (DateTimeField) Fecha de la última actualización realizada al grupo.
    """
    name = models.CharField(verbose_name='Nombre de la rutina', max_length=120)

    created_at = models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha de actualización', auto_now=True)
