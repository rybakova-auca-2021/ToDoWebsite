from django.urls import path, include
from .views import HomePage, Register, Login, logout_view
from .views import toDoAppView, addToDoView, deleteItemView

urlpatterns = [
    path('home/', HomePage, name='home-page'),
    path('register/', Register, name='register-page'),
    path('login/', Login, name='login-page'),
    path('list/', toDoAppView, name='list'),
    path('addItem/', addToDoView, name='addItem'), 
    path('deleteItem/<int:i>/', deleteItemView, name='deleteItem')
]