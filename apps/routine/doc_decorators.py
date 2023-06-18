from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from apps.routine.serializers import RoutineSerializer


# Decoradores
def doc_view_routine_retrieve(action):
    """
    This decorator purpose is to reuse the auto schema.
    """
    retrieve_responses = {
        401: 'El usuario debe estar autenticado',
        201: openapi.Response('response description', RoutineSerializer()),
    }

    return swagger_auto_schema(responses=retrieve_responses)(action)


def doc_view_routine_create(action):
    """
    This decorator purpose is to reuse the auto schema.
    """
    create_responses = {
        400: 'Los parámetros deben ser correctos.',
        401: 'El usuario debe estar autenticado',
        201: openapi.Response('response description', RoutineSerializer()),
    }

    return swagger_auto_schema(responses=create_responses)(action)


def doc_view_routine_partial_update(action):
    """
    This decorator purpose is to reuse the auto schema.
    """
    partial_update_responses = {
        400: 'Los parámetros deben ser correctos.',
        401: 'El usuario debe estar autenticado',
        200: openapi.Response('response description', RoutineSerializer()),
    }

    return swagger_auto_schema(responses=partial_update_responses)(action)


def doc_view_routine_destroy(action):
    """
    This decorator purpose is to reuse the auto schema.
    """
    destroy_responses = {
        401: 'El usuario debe estar autenticado',
        204: openapi.Response('response description', RoutineSerializer()),
    }

    return swagger_auto_schema(responses=destroy_responses)(action)
