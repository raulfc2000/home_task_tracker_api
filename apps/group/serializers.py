from rest_framework import serializers

from apps.group.models import Group


class GroupSerializer(serializers.ModelSerializer):
    """
    Serializer de Group
    """
    class Meta:
        model = Group
        fields = (
            'id',
            'user_owner',
            'user_list',
            # 'routine', TODO poner cuando routine esté hecho
            'created_at',
            'updated_at',
        )

        read_only_fields = (
            'id',
            'user_owner',
            'created_at',
            'updated_at',
        )

    def create(self, validated_data):
        # Obtener el usuario de la petición.
        user = self.context['request'].user

        # Asociarlo al user_owner y añadirlo al listado de usuarios.
        validated_data['user_owner'] = user
        validated_data['users_list'].append(user)

        return super().create(validated_data)
