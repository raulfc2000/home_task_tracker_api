from django.shortcuts import render
from rest_framework import viewsets

from apps.group.models import Group


class GroupView(viewsets.ModelViewSet):
    """
    View de Group
    """
    queryset = Group.objects.all()
