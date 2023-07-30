from django.urls import path, include
from .views import HomePage, Register, Login, logout_view

urlpatterns = [
    path('home/', HomePage, name='home-page'),
    path('register/', Register, name='register-page'),
    path('login/', Login, name='login-page')
]