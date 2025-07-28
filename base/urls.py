from django.urls import path
from .views import TaskList,TaskDetail,TaskCreate,TaskUpdate,TaskDelete
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('',TaskList.as_view(),name='tasks'),
    path('task/<int:pk>',TaskDetail.as_view(),name='task'),
    path('create/',TaskCreate.as_view(),name='create-task'),
    path('update/<int:pk>/',TaskUpdate.as_view(),name='task-update'),
    path('delete/<int:pk>/',TaskDelete.as_view(),name='task-delete'),
]
