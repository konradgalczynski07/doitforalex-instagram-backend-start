from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from users.serializers import (
    UserSerializer,
    RegisterUserSerializer,
    UserProfileSerializer,
)


User = get_user_model()


class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = (permissions.AllowAny,)


class UserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class UserProfileView(generics.RetrieveAPIView):
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.AllowAny,)


class FollowUserView(APIView):
    def get(self, request, format=None, username=None):
        to_user = User.objects.get(username=username)
        from_user = self.request.user
        follow = None
        if from_user != to_user:
            if from_user in to_user.followers.all():
                follow = False
                from_user.following.remove(to_user)
                to_user.followers.remove(from_user)
            else:
                follow = True
                from_user.following.add(to_user)
                to_user.followers.add(from_user)
        data = {'follow': follow}
        return Response(data)
