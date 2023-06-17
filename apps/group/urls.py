from django.urls import path
from apps.group import views

urlpatterns = [
    path('', views.GroupView.as_view({'get': 'list', 'post': 'create'}), name='groups'),
    path('<int:pk>/', views.GroupView.as_view(
        {
            'get': 'retrieve',
            'patch': 'partial_update',
            'delete': 'destroy'
        }
    ), name='groups_detail'),
]
