from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.http import JsonResponse
from ..models import Message, ConversationParticipant, User, Conversation
from ..serializers import MessageSerializer
from ..utils.decode_token import decode_token
from rest_framework.permissions import IsAuthenticated
from django.utils.timezone import now
import json


@api_view(["GET"])
def get_messages_general_chat(request):
    user_id, error_response = decode_token(request)
    # user = request.user
    conversations = ConversationParticipant.objects.filter(user_id=user_id).values_list(
        "conversation_id", flat=True
    )
    messages = Message.objects.filter(conversation_id__in=conversations).order_by(
        "timestamp"
    )

    message_list = [
        {
            "id": msg.id,
            "sender_id": msg.sender.id,
            "fullname": msg.sender.fullname,
            "profile_pic": msg.sender.profile_pic,
            "content": msg.content,
            "timestamp": msg.timestamp,
        }
        for msg in messages
    ]

    return JsonResponse({"messages": message_list})


@api_view(["GET"])
def get_messages_gemini(request):
    user_id, error_response = decode_token(request)
    if error_response:
        return error_response
    user = User.objects.get(id=user_id)

    try:
        User.objects.get(username="Gemini")
    except User.DoesNotExist:
        return JsonResponse({"error": "AI user not found"}, status=404)

    conversation, created = Conversation.objects.get_or_create(
        name=f"Gemini with {user.username}"
    )

    if created:
        return JsonResponse({"messages": []})

    messages = Message.objects.filter(conversation=conversation).order_by("timestamp")

    message_list = [
        {
            "id": msg.id,
            "sender_id": msg.sender.id,
            "fullname": msg.sender.fullname,
            "profile_pic": msg.sender.profile_pic,
            "content": msg.content,
            "timestamp": msg.timestamp,
        }
        for msg in messages
    ]

    return JsonResponse({"messages": message_list})


@api_view(["POST"])
def save_message_gemini(request):
    user_id, error_response = decode_token(request)
    if error_response:
        return error_response
    user = User.objects.get(id=user_id)
    print(f"hi {user}")
    print(f"Raw body: {request.body}")

    try:
        data = json.loads(request.body.decode("utf-8"))
        messages = data.get("messages", [])
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON format"}, status=400)

    gemini_user, _ = User.objects.get_or_create(username="Gemini")

    conversation, _ = Conversation.objects.get_or_create(
        name=f"Gemini with {user.username}"
    )

    saved_messages = []
    for msg in messages:
        sender = user if msg["sender"] == user.id else gemini_user
        message = Message.objects.create(
            sender=sender,
            conversation=conversation,
            content=msg["content"].replace("\n", ""),
            timestamp=now(),
        )
        saved_messages.append(
            {
                "id": message.id,
                "sender": message.sender.username,
                "content": message.content,
                "timestamp": message.timestamp,
                "conversation_id": message.conversation.id,
            }
        )

    return JsonResponse({"message": "Messages saved successfully"}, status=201)
