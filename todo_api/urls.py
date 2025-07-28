from django.urls import path
from .views import TaskView,TaskCreate,TaskUpdate,TaskDelete

urlpatterns = [
    path('',TaskView.as_view(),name = 'TaskView'),
    path('create/',TaskCreate.as_view(),name = 'TaskCreate'),
    path('update/<int:pk>/',TaskUpdate.as_view(),name = 'TaskUpdate'),
    path('delete/<int:pk>/',TaskDelete.as_view(),name = 'TaskDelete'),
]
