from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import User
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password, make_password


@api_view(["GET"])
@permission_classes([AllowAny])
def get_users():
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    print(f"Received - Username: {username}, Password: {password}")

    if not username or not password:
        return Response(
            {"error": "Username và password no đủ"}, status=status.HTTP_400_BAD_REQUEST
        )
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response(
            {"error": "Sai username or password"}, status=status.HTTP_401_UNAUTHORIZED
        )

    if check_password(password, user.password):
        return Response(
            {
                "message": "Success",
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                },
            },
            status=status.HTTP_200_OK,
        )
    else:
        return Response(
            {"error": "Sai username or password"}, status=status.HTTP_401_UNAUTHORIZED
        )


@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):
    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email")

    if not username or not password or not email:
        return Response({"error": "missing data"}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response(
            {"error": "Username đã tồn tại"}, status=status.HTTP_400_BAD_REQUEST
        )

    user = User.objects.create(
        username=username, email=email, password=make_password(password)
    )

    return Response(
        {
            "message": "Success",
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            },
        },
        status=status.HTTP_201_CREATED,
    )
