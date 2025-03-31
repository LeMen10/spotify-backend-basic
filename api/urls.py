from django.urls import path
from .views.auth_views import register, login
from .views.user_views import get_users, user_profile, get_user
from .views.message_views import (
    get_messages_general_chat,
    get_messages_gemini,
    save_message_gemini,
    save_message_general,
)
from .views.conversation_views import get_conversation

urlpatterns = [
    # auth
    path("auth/login", login, name="user-login"),
    path("auth/register", register, name="user-register"),
    # users
    path("user/get-users", get_users, name="user-list"),
    path("user/get-user", get_user, name="user"),
    path("user/user-profile", user_profile, name="user-profile"),
    # messages
    path(
        "message/get-messages-general-chat",
        get_messages_general_chat,
        name="message-list",
    ),
    path("message/get-messages-gemini", get_messages_gemini, name="message-list-AI"),
    path("message/save-messages-gemini", save_message_gemini, name="save-message-AI"),
    path("message/save-message-general", save_message_general, name="send-message-general"),

    #conversation
    path("conversation/get-conversation", get_conversation, name="get-conversation"),
]
