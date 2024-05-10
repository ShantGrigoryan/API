from .models import *
from rest_framework import serializers

class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = '__all__'

class TasksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tasks
        fields = '__all__'