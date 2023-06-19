from django.contrib.auth.models import User
from rest_framework import serializers

from apps.task.models import Task


class UserTaskSerializer(serializers.ModelSerializer):
    """
    Serializer de usuario para utilizarlo en Group
    """
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email'
        )

        read_only_fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
        )


class UserPKRelatedField(serializers.PrimaryKeyRelatedField):
    def to_representation(self, value):
        user = User.objects.get(pk=value.pk)
        user_serialized = UserTaskSerializer(user)

        return user_serialized.data


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer de Task

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
    created_by = UserTaskSerializer(read_only=True)
    assigned_to = UserPKRelatedField(
        queryset=User.objects.all(),
        required=True,
    )

    class Meta:
        model = Task
        fields = (
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

        read_only_fields = (
            'id',
            'created_by',
            'created_at',
            'updated_at',
        )

    def create(self, validated_data):
        # Obtener el usuario de la petición.
        user = self.context['request'].user

        # Asociarlo al created_by.
        validated_data['created_by'] = user

        return super().create(validated_data)
