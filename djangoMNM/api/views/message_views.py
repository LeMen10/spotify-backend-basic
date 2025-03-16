from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from ..models import Message
from ..serializers import MessageSerializer

@api_view(["GET"])
@permission_classes([AllowAny])
def get_messages(request):
    messages = Message.objects.select_related("sender", "group").all()
    
    data = [
        {
            "id": msg.id,
            "sender_id": msg.sender.id,
            "username": msg.sender.username,
            "group_id": msg.group.id,
            "group_name": msg.group.name,
            "content": msg.content,
        }
        for msg in messages
    ]

    return Response(data)
