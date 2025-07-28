from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import task
from django.contrib.auth.mixins import LoginRequiredMixin


class TaskList(LoginRequiredMixin,ListView):
    model = task
    template_name = 'base/taskview.html'
    context_object_name = 'tasks'
    ordering = ['-created']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        if query:
            context['tasks'] = task.objects.filter(user = self.request.user,title__icontains = query)
        else:
            context['tasks'] = task.objects.filter(user = self.request.user)
        return context

class TaskDetail(LoginRequiredMixin,DetailView):
    model = task
    template_name = 'base/task_detail.html'
    context_object_name = 'task'

class TaskCreate(LoginRequiredMixin,CreateView):
    model = task
    fields = ['title','description','complete']
    template_name = 'base/create_task.html'
    success_url = reverse_lazy('tasks')

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = task
    fields = ['title','description','complete']
    template_name = 'base/update_task.html'
    success_url = reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin,DeleteView):
    model = task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    template_name = 'base/task_delete.html'
