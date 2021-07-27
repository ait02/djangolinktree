from django.urls import path
from .views import index, myLinks, register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name="index"),
    path('login/', auth_views.LoginView.as_view(template_name='frontend/login.html'), name="login"),
    path('register/', register, name="register"),
    path('<str:username>/', myLinks, name="my-links"),
]