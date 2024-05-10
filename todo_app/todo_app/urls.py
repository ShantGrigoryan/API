# todo_app/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from main.views import UsersAPI, TasksAPI

router = routers.DefaultRouter()
router.register(r'users', UsersAPI)
router.register(r'tasks', TasksAPI)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
