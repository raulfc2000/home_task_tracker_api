from django.contrib.auth.models import User
from django.db import models

from apps.routine.models import Routine


class Task(models.Model):
    """
    Modelo Task
    - id: (IntegerField) Número entero, único y auto-incremental, asignado automáticamente.
    - routine: (ForeignKey) Rutina a la que pertenece la tarea.
    - title: (CharField) Título de la tarea que se realizará.
    - description: (TextField) Campo de texto no obligatorio que dará una descripción sobre lo que se realizará.
    - starts_at: (DateTimeField) Fecha y hora a la que comienza la tarea.
    - created_by: (ForeignKey) Usuario que ha creado la tarea (se asignará automáticamente mediante el serializador).
    - assigned_to: (ForeignKey) Usuario que realizará la tarea.
    - completed: (BooleanField) Booleano que indica si la tarea está terminada o no.

    - created_at: (DateTimeField) Fecha en la cual se creó el grupo.
    - updated_at: (DateTimeField) Fecha de la última actualización realizada al grupo.
    """
    routine = models.ForeignKey(Routine, verbose_name='Rutina', on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(verbose_name='Título', max_length=100)
    description = models.TextField(verbose_name='Descripción', max_length=2048, null=True, blank=True)
    starts_at = models.DateTimeField(verbose_name='Fecha y hora de inicio')
    created_by = models.ForeignKey(User,
                                   verbose_name='Usuario que ha creado la tarea',
                                   null=True,
                                   related_name='tasks_created',
                                   on_delete=models.SET_NULL)
    assigned_to = models.ForeignKey(User,
                                    verbose_name='Usuario que realizará la tarea',
                                    null=True,
                                    related_name='assigned_tasks',
                                    on_delete=models.SET_NULL)
    completed = models.BooleanField(verbose_name='Completada', default=False)

    created_at = models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha de actualización', auto_now=True)
