from rest_framework import serializers

from apps.routine.models import Routine
from apps.task.serializers import TaskSerializer


class RoutineSerializer(serializers.ModelSerializer):
    """
    Serializer de Routine
    """

    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Routine
        fields = (
            'id',
            'name',
            'group',
            'tasks',
            'created_at',
            'updated_at',
        )

        read_only_fields = (
            'id',
            'tasks',
            'created_at',
            'updated_at',
        )
