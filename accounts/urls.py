from django.urls import path
from .views import CustomSignup
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('signup/',CustomSignup.as_view(),name = 'signup'),
    path('login/',LoginView.as_view(template_name = 'accounts/login.html'),name = 'login'),
    path('logout/',LogoutView.as_view(),name = 'logout'),
]
