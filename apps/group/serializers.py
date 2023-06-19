from django.contrib.auth.models import User
from rest_framework import serializers

from apps.group.models import Group
from apps.routine.serializers import RoutineSerializer


class UserGroupSerializer(serializers.ModelSerializer):
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
        user_serialized = UserGroupSerializer(user)

        return user_serialized.data


class GroupSerializer(serializers.ModelSerializer):
    """
    Serializer de Group
    """
    user_owner = UserGroupSerializer(read_only=True)
    users_list = UserPKRelatedField(
        queryset=User.objects.all(),
        many=True,
        required=False,
    )
    routines = RoutineSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = (
            'id',
            'name',
            'user_owner',
            'users_list',
            'routines',
            'created_at',
            'updated_at',
        )

        read_only_fields = (
            'id',
            'user_owner',
            'routines',
            'created_at',
            'updated_at',
        )

    def create(self, validated_data):
        # Obtener el usuario de la petición.
        user = self.context['request'].user

        # Asociarlo al user_owner y añadirlo al listado de usuarios.
        validated_data['user_owner'] = user

        validated_data['users_list'] = []
        validated_data['users_list'].append(user)

        return super().create(validated_data)
