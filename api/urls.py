from django.urls import path
from .views.auth_views import register, login
from .views.user_views import get_users_test, user_profile, get_user
from .views.message_views import (
    get_messages_general_chat,
    get_messages_gemini,
    save_message_gemini,
    save_message_general,
)
from .views.conversation_views import get_conversation
from .views.song_views import get_songs
from django.conf import settings
from django.conf.urls.static import static
from .views.admin.music_management_view import (
    add_song,
    get_songs_management,
    update_song,
    delete_song,
)
from .views.admin.artist_management_view import (
    get_artists,
    add_artist,
    update_artist,
    delete_artist,
)
from .views.admin.genres_management_view import (
    get_genres,
    add_genre,
    update_genre,
    delete_genre,
)
from .views.admin.user_management_view import (
    get_users,
    add_user,
    update_user,
    delete_user,
)

urlpatterns = [
    # auth
    path("auth/login", login, name="user-login"),
    path("auth/register", register, name="user-register"),
    # users
    path("user/get-users", get_users_test, name="user-list"),
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
    path(
        "message/save-message-general",
        save_message_general,
        name="send-message-general",
    ),
    # conversation
    path("conversation/get-conversation", get_conversation, name="get-conversation"),
    # song
    path("songs/get-songs", get_songs, name="song-list"),
    path("songs/add", add_song, name="add-song"),
    # admin song
    path("admin/get-songs", get_songs_management, name="song-list"),
    path("admin/add-song", add_song, name="add-song"),
    path("admin/update-song/<int:song_id>/", update_song, name="update-song"),
    path("admin/delete-song/<int:song_id>", delete_song, name="delete-song"),
    # admin artist
    path("admin/get-artists", get_artists, name="artist-list"),
    path("admin/add-artist", add_artist, name="add_artist"),
    path("admin/update-artist/<int:id>", update_artist, name="update_artist"),
    path("admin/delete-artist/<int:id>", delete_artist, name="delete_artist"),
    # admin genres
    path("admin/get-genres", get_genres, name="genre-list"),
    path("admin/add-genre", add_genre, name="add_genre"),
    path("admin/update-genre/<int:id>", update_genre, name="update_genre"),
    path("admin/delete-genre/<int:id>", delete_genre, name="delete_genre"),
    # admin user
    path("admin/get-users", get_users, name="user-list"),
    path("admin/add-user", add_user, name="add-user"),
    path("admin/update-user/<int:user_id>", update_user, name="update-user"),
    path("admin/delete-user/<int:user_id>", delete_user, name="delete-user"),
]
