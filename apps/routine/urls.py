from django.urls import path
from apps.routine import views

urlpatterns = [
    path('', views.RoutineView.as_view({'post': 'create'}), name='routines'),
    path('<int:pk>/', views.RoutineView.as_view(
        {
            'get': 'retrieve',
            'patch': 'partial_update',
            'delete': 'destroy'
        }
    ), name='routines_detail'),
]
