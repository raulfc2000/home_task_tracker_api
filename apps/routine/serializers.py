from rest_framework import serializers

from apps.routine.models import Routine


class RoutineSerializer(serializers.ModelSerializer):
    """
    Serializer de Routine
    """

    class Meta:
        model = Routine
        fields = (
            'id',
            'name',
            'group',
            'created_at',
            'updated_at',
        )

        read_only_fields = (
            'id',
            'created_at',
            'updated_at',
        )
