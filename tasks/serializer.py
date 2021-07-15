from rest_framework import serializers
from .models import Task, BT


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class BTSerializer(serializers.ModelSerializer):
    class Meta:
        model = BT
        fields = '__all__'
