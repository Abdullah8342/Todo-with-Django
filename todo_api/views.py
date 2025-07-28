from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView
from django.contrib.auth.mixins import LoginRequiredMixin
from .serializers import TaskSerializer
from .models import Task
# Create your views here.

class TaskView(LoginRequiredMixin,ListAPIView):

    def get_queryset(self):
        return Task.objects.filter(user = self.request.user)

    def get_serializer_class(self):
        return TaskSerializer

    def get_serializer_context(self):
        return {'user':self.request.user}


class TaskCreate(LoginRequiredMixin,CreateAPIView):

    def get_queryset(self):
        return Task.objects.filter(user = self.request.user)

    def get_serializer_class(self):
        return TaskSerializer

    def get_serializer_context(self):
        return {'user':self.request.user}


class TaskUpdate(LoginRequiredMixin,RetrieveUpdateAPIView):
    def get_queryset(self):
        return Task.objects.filter(user = self.request.user)

    def get_serializer_class(self):
        return TaskSerializer

    def get_serializer_context(self):
        return {'user':self.request.user}


class TaskDelete(LoginRequiredMixin,RetrieveDestroyAPIView):
    def get_queryset(self):
        return Task.objects.filter(user = self.request.user)

    def get_serializer_class(self):
        return TaskSerializer

    def get_serializer_context(self):
        return {'user':self.request.user}
