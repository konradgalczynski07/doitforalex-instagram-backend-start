from rest_framework import generics, permissions
from users.serializers import RegisterUserSerializer


class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = (permissions.AllowAny,)
