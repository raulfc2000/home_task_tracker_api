"""
URL configuration for home_task_tracker_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# AUTH (https://dj-rest-auth.readthedocs.io/en/latest/introduction.html)
dj_rest_auth_path = path('auth/', include('dj_rest_auth.urls'))
# TODO importante url para el password reset
dj_rest_auth_path_registration = path('auth/registration/', include('dj_rest_auth.registration.urls'))
# TODO ¿social authentication? ej. Iniciar Sesión con Google

# SWAGGER (https://django-rest-swagger.readthedocs.io/en/latest/)
api_info = openapi.Info(
    title="Home Task Tracker Backend",
    default_version='v1',
    terms_of_service="TODO",
    contact=openapi.Contact(email="yanngelmarbella@gmail.com"),
)
schema_view = get_schema_view(
    info=api_info,
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    dj_rest_auth_path,
    dj_rest_auth_path_registration,
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('group/', include('apps.group.urls')),
]
