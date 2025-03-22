from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from datetime import datetime, timedelta, timezone
from django.contrib.auth.hashers import check_password, make_password
from ..models import User
from api.utils.generate_token import generate_jwt_token


@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    print(username, password)

    if not username or not password:
        return Response(
            {"error": "missing username or password"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        user = User.objects.get(username=username)
        print(user.__dict__)
    except User.DoesNotExist:
        return Response(
            {"error": "fail username or password"}, status=status.HTTP_401_UNAUTHORIZED
        )

    if check_password(password, user.password):
        token, expires_at  = generate_jwt_token(user)
        return Response(
            {
                "message": "Success",
                "access_token": token,
                "expires_at": expires_at,
            },
            status=status.HTTP_200_OK,
        )

    return Response(
        {"error": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED
    )


@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):
    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email")
    fullname = request.data.get("fullname")
    profile_pic = request.data.get("profile_pic")

    if not username or not password or not email or not fullname:
        return Response({"error": "missing data"}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response(
            {"error": "username already exists"}, status=status.HTTP_400_BAD_REQUEST
        )

    User.objects.create(
        username=username,
        email=email,
        password=make_password(password),
        fullname=fullname,
        profile_pic=profile_pic,
    )

    return Response({"message": "Success"}, status=status.HTTP_201_CREATED)
