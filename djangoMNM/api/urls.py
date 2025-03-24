from django.urls import path
<<<<<<< Updated upstream
from .views import  UserListAPIView

urlpatterns = [
    path('users/', UserListAPIView.as_view(), name='user-list'),
=======
from .views.auth_views import register, login
from .views.user_views import get_users, user_profile, get_user
from .views.message_views import get_messages_general_chat, get_messages_gemini, save_message_gemini

urlpatterns = [
    # auth
    path('auth/login', login, name='user-login'),
    path('auth/register', register, name='user-register'),

    # users
    path('user/get-users', get_users, name='user-list'),
    path('user/get-user', get_user, name='user'),
    path('user/user-profile', user_profile, name='user-profile'),

    # messages
    path('message/get-messages-general-chat', get_messages_general_chat, name='message-list'),
    path('message/get-messages-gemini', get_messages_gemini, name='message-list-AI'),
    path('message/save-messages-gemini', save_message_gemini, name='save-message-AI'),
>>>>>>> Stashed changes
]
