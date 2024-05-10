from django.shortcuts import render
from rest_framework import generics
from .models import *
from rest_framework import viewsets
from .serializers import *
# Create your views here.

class UsersAPI(viewsets.ModelViewSet):

    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class TasksAPI(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer