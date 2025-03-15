from django.urls import path
from .views import register, login, get_users

urlpatterns = [
    # auth
    path('auth/login', login, name='user-login'),
    path('auth/register', register, name='user-register'),

    # users
    path('user/get-users', get_users, name='user-list'),
]
