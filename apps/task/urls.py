from django.urls import path
from apps.task import views

urlpatterns = [
    path('', views.TaskView.as_view({'get': 'list', 'post': 'create'}), name='tasks'),
    path('<int:pk>/', views.TaskView.as_view(
        {
            'get': 'retrieve',
            'patch': 'partial_update',
            'delete': 'destroy'
        }
    ), name='tasks_detail'),
]
