from ..models import Song
from ..serializers import SongSerializer
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from ..utils.decode_token import decode_token

@api_view(['GET'])
@permission_classes([AllowAny])
def get_songs(request):
    songs = Song.objects.all()
    serializer = SongSerializer(songs, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(["POST"])
@permission_classes([AllowAny])
@parser_classes([MultiPartParser, FormParser])  # Hỗ trợ upload file
def add_song(request):
    try:
        title = request.data.get("title")
        duration = request.data.get("duration")
        release_date = request.data.get("release_date")
        artist_id = request.data.get("artist_id")
        genre_id = request.data.get("genre_id")
        audio_file = request.FILES.get("audio_file")  # Lấy file từ request

        if not all([title, duration, release_date, artist_id, genre_id, audio_file]):
            return Response({"error": "Missing fields"}, status=400)

        song = Song.objects.create(
            title=title,
            duration=duration,
            release_date=release_date,
            artist_id=artist_id,
            genre_id=genre_id,
            audio_file=audio_file
        )

        return Response(SongSerializer(song).data, status=201)
    except Exception as e:
        return Response({"error": str(e)}, status=500)