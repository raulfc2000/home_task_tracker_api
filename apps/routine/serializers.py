from rest_framework import serializers

from apps.group.models import Group


class RoutineSerializer(serializers.ModelSerializer):
    """
    Serializer de Routine
    """

    # group = serializers.PrimaryKeyRelatedField()  TODO comprobar si por defecto lo hace así

    class Meta:
        model = Group
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
