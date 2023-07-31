from django.urls import path, include
from .views import HomePage, Register, Login, logout_view
from .views import to_do_app_view, add_to_do_view, delete_item_view

urlpatterns = [
    path('home/', HomePage, name='home-page'),
    path('register/', Register, name='register-page'),
    path('login/', Login, name='login-page'),
    path('list/', to_do_app_view, name='list'),
    path('addItem/', add_to_do_view, name='addItem'), 
    path('deleteItem/<int:i>/', delete_item_view, name='deleteItem')
]