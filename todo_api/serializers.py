from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only = True)
    user = serializers.CharField(read_only = True)
    class Meta:
        model = Task
        fields = ['id','user','title','description','complete','created']

    def create(self, validated_data):
        validated_data['user'] = self.context['user']
        return super().create(validated_data)
