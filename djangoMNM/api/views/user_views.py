from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.http import HttpResponse
from ..models import User
from ..serializers import UserSerializer
from rest_framework import status
from ..middleware.decode_token import DecodeTokenMiddleware


@api_view(["GET"])
@permission_classes([AllowAny])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@DecodeTokenMiddleware
@permission_classes([IsAuthenticated])
def user_profile(request):
    print("request:", request.user_id)
    if not request.user.is_authenticated:
        return HttpResponse("No login!")
    return Response(
        {
            "message": "Success",
            "user": str(request.user),
        },
        status=status.HTTP_200_OK,
    )


@api_view(["GET"])
@DecodeTokenMiddleware
@permission_classes([IsAuthenticated])
def get_user(request):
    print("request:", request.user.__dict__)
    user = request.user.__dict__
    if not request.user.is_authenticated:
        return HttpResponse("No login!")
    return Response(
        {
            "message": "Success",
            "user": {
                "id": user.get("id"),
                "username": user.get("username"),
                "profile_pic": (
                    str(user.get("profile_pic")) if user.get("profile_pic") else None
                ),
            },
        },
        status=status.HTTP_200_OK,
    )
