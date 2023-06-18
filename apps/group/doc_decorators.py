from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from apps.group.serializers import GroupSerializer


# Decoradores


def doc_view_group_list(action):
    """
    This decorator purpose is to reuse the auto schema.
    """
    list_param = [
        openapi.Parameter('search', openapi.IN_QUERY,
                          description='Campos de búsqueda: name',
                          type=openapi.TYPE_STRING),
        openapi.Parameter('filter', openapi.IN_QUERY,
                          description='Campos de filtrado: name',
                          type=openapi.TYPE_STRING),
        openapi.Parameter('ordering', openapi.IN_QUERY,
                          description='Campos de ordenación: created_at, updated_at',
                          type=openapi.TYPE_STRING)
    ]

    list_responses = {
        401: 'El usuario debe estar autenticado',
        200: openapi.Response('response description', GroupSerializer(many=True)),
    }
    return swagger_auto_schema(manual_parameters=list_param, responses=list_responses)(action)


def doc_view_group_retrieve(action):
    """
    This decorator purpose is to reuse the auto schema.
    """
    retrieve_responses = {
        401: 'El usuario debe estar autenticado',
        201: openapi.Response('response description', GroupSerializer()),
    }

    return swagger_auto_schema(responses=retrieve_responses)(action)


def doc_view_group_create(action):
    """
    This decorator purpose is to reuse the auto schema.
    """
    create_responses = {
        400: 'Los parámetros deben ser correctos.',
        401: 'El usuario debe estar autenticado',
        201: openapi.Response('response description', GroupSerializer()),
    }

    return swagger_auto_schema(responses=create_responses)(action)


def doc_view_group_partial_update(action):
    """
    This decorator purpose is to reuse the auto schema.
    """
    partial_update_responses = {
        400: 'Los parámetros deben ser correctos.',
        401: 'El usuario debe estar autenticado',
        200: openapi.Response('response description', GroupSerializer()),
    }

    return swagger_auto_schema(responses=partial_update_responses)(action)


def doc_view_group_destroy(action):
    """
    This decorator purpose is to reuse the auto schema.
    """
    destroy_responses = {
        401: 'El usuario debe estar autenticado',
        204: openapi.Response('response description', GroupSerializer()),
    }

    return swagger_auto_schema(responses=destroy_responses)(action)
