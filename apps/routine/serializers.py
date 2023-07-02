from rest_framework import serializers

from apps.group.models import Group
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

    def validate(self, data):
        """
        Función para validar condiciones adicionales
        """
        # ARRANGE
        user_id = self.context['request'].user.id
        group = data['group']
        group_users_list_ids = group.users_list.values_list('id', flat=True)

        # Si el ID de usuario no está en el listado de IDs de los usuarios del grupo, is_valid() no es True
        if user_id not in group_users_list_ids:
            raise serializers.ValidationError('User must be in group')

        return data
