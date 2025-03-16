from django.urls import path
from .views.auth_views import register, login
from .views.user_views import get_users
from .views.message_views import get_messages

urlpatterns = [
    # auth
    path('auth/login', login, name='user-login'),
    path('auth/register', register, name='user-register'),

    # users
    path('user/get-users', get_users, name='user-list'),

    # messages
    path('message/get-messages', get_messages, name='message-list'),
]
