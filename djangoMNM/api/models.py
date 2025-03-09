from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'users'


class Artist(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "artists"


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = "genres"


class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    duration = models.PositiveIntegerField()
    release_date = models.DateField(null=True, blank=True)
    genre = models.ForeignKey(Genre, null=True, blank=True, on_delete=models.SET_NULL)
    play_count = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "songs"


class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "playlists"


class PlaylistSong(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    class Meta:
        db_table = "playlist_songs"
        unique_together = ("playlist", "song")


class GroupMessage(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "group_messages"


class GroupMember(models.Model):
    group = models.ForeignKey(GroupMessage, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "group_members"


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(GroupMessage, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "messages"
