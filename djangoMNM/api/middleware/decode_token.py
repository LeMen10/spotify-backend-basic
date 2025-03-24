import jwt
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from functools import wraps

User = get_user_model()

EXCLUDED_PATHS = [
    "/api/user/get-users",
    "/api/auth/login",
    "/api/auth/register",
]

def DecodeTokenMiddleware(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        print(f"Middleware chạy cho: {request.get_full_path()}")
        if any(request.get_full_path().startswith(path) for path in EXCLUDED_PATHS):
            return view_func(request, *args, **kwargs)
        
        token = request.headers.get("Authorization")
        if not token:
            return JsonResponse({"error": "no token"}, status=401)

        try:
            if token.startswith("Bearer "):
                token = token.split(" ")[1]

            decoded_payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms=["HS256"]
            )

            user_id = decoded_payload.get("id")
            try:
                user = User.objects.get(id=int(user_id))
                request.user = user
                request.user_id = user_id
            except User.DoesNotExist:
                return JsonResponse({"error": "User no tồn tại"}, status=401)

        except jwt.ExpiredSignatureError:
            return JsonResponse({"error": "Token đã hết hạn"}, status=401)

        except jwt.InvalidTokenError:
            return JsonResponse({"error": "Token no hợp lệ"}, status=401)

        return view_func(request, *args, **kwargs)

    return _wrapped_view


# import jwt
# from django.conf import settings
# from django.http import JsonResponse
# from django.utils.deprecation import MiddlewareMixin
# from django.contrib.auth import get_user_model

# User = get_user_model()


# class DecodeTokenMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         token = request.headers.get("Authorization")

#         if token:
#             try:
#                 if token.startswith("Bearer "):
#                     token = token.split(" ")[1]

#                 decoded_payload = jwt.decode(
#                     token, settings.SECRET_KEY, algorithms=["HS256"]
#                 )
#                 print(decoded_payload)
#                 print(User._meta.db_table)

#                 # Lấy user từ database
#                 user_id = decoded_payload.get("id")
#                 print(user_id)
#                 print(f"User ID từ JWT: {user_id} ({type(user_id)})")
#                 try:
#                     user = User.objects.get(id=int(user_id))
#                     print(user)
#                     request.user = user
#                 except User.DoesNotExist:
#                     return JsonResponse({"error": "User no tồn tại"}, status=401)

#             except jwt.ExpiredSignatureError:
#                 return JsonResponse({"error": "Token đã hết hạn"}, status=401)

#             except jwt.InvalidTokenError:
#                 return JsonResponse({"error": "Token no hợp lệ"}, status=401)

#         return None
