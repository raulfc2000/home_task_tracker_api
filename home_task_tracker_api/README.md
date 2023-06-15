# Información General

Home Task Tracker Api es una API pensada para poder registrar grupos de usuarios en los cuales gestionar las tareas del
piso.

## Módulos

    - Group: 
    Grupos de usuarios creados por usuarios. 
    - Routine
    - Task

## Permisos

    Por defecto:
    - AllowAny (Permite realizar la petición a cualquier usuario, autenticado o no)
    - IsAuthenticated (Permite realizar la petición únicamente a los usuarios autenticados)
    - IsSuperUser (Permite realizar la petición únicamente a los superusuarios)
[//]: # (Ver si es estrictamente necesario el permiso IsOwnUser)
    Customs:
    - IsOwnUser (El usuario que se quiere modificar es el propio usuario)
    - IsInGroup (El usuario que realiza la petición está en el grupo de la Routine)

## Testeo

    - Filter (testeos unitarios a los filtros de las views con la librería pytest)
    - Serializer (testeos unitarios a los serializadores con la librería django.test)
    - Integración (testeos de integración a las urls y views que simularán el recorrido entero de una petición en la
      API)
    - Utils (Si da tiempo, poner testeo en general de funciones usadas en el proyecto, sino se hará en las siguientes
      versiones)

## Autor

    Esta API ha sido realizada por Raúl Fernández Cruz, realizando su primera versión para el Proyecto Integrado del
    FP Superior de Desarrollo de Aplicaciones Multiplataformas en el IES Belén.


# Peticiones y urls

Todas las peticiones y urls están en swagger.
Para acceder al swagger, en un navegador web accede al endpoint: http://127.0.0.1:8000/swagger/

## Auth

    Login:
    - http://127.0.0.1:8000/login/ (POST)
    - http://127.0.0.1:8000/logout/ (POST)
    
    Password:
    - http://127.0.0.1:8000/password/change/ (POST)
    
    Para las próximas versiones (con server de correo):
    - http://127.0.0.1:8000/password/reset/ (POST)
    - http://127.0.0.1:8000/password/reset/confirm/ (POST)
    
    Registration:
    - http://127.0.0.1:8000/registration/ (POST)

    Para las próximas versiones (con server de correo):
    - http://127.0.0.1:8000/registration/resend-email/ (POST)
    - http://127.0.0.1:8000/registration/verify-email/ (POST)

## User

    - http://127.0.0.1:8000/user/ (GET)
    - http://127.0.0.1:8000/user/ (PUT)
    - http://127.0.0.1:8000/user/ (PATCH)


## Group

    - http://127.0.0.1:8000/group/ (GET)
    - http://127.0.0.1:8000/group/ (POST)
    - http://127.0.0.1:8000/group/<int:pk>/ (GET)
    - http://127.0.0.1:8000/group/<int:pk>/ (PATCH)

## Routine

    - http://127.0.0.1:8000/routine/ (GET)
    - http://127.0.0.1:8000/routine/ (POST)
    - http://127.0.0.1:8000/routine/<int:pk>/ (GET)
    - http://127.0.0.1:8000/routine/<int:pk>/ (PATCH)


## Task

    - http://127.0.0.1:8000/task/ (GET)
    - http://127.0.0.1:8000/task/ (POST)
    - http://127.0.0.1:8000/task/<int:pk>/ (GET)
    - http://127.0.0.1:8000/task/<int:pk>/ (PATCH)
