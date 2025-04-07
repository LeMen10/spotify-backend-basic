from rest_framework import serializers
from .models import User, Message, Conversation, Song
from django.conf import settings
from urllib.parse import unquote


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "fullname", "profile_pic"]


class MessageSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Message
        fields = ["id", "sender", "group", "content", "timestamp"]


class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = "__all__"


class SongSerializer(serializers.ModelSerializer):
    audio_url = serializers.SerializerMethodField()
    artist_info = serializers.SerializerMethodField()
    genre_info = serializers.SerializerMethodField()

    class Meta:
        model = Song
        fields = fields = [
            'id', 'title', 'duration', 'release_date',
            'play_count', 'audio_url', 'artist_info', 'genre_info'
        ]

    def get_audio_url(self, obj):
        if not obj.audio_file:
            return None
        
        request = self.context.get('request')
        url = obj.audio_file.url
        decoded_url = unquote(url)
        
        if request:
            return request.build_absolute_uri(decoded_url)
        return f"{settings.BASE_URL}{decoded_url}"
    
    def get_artist_info(self, obj):
        return {'id': obj.artist.id, 'name': obj.artist.name}

    def get_genre_info(self, obj):
        return {'id': obj.genre.id, 'name': obj.genre.name}
