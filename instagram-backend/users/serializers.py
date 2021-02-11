from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'fullname', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 5},
            'username': {'min_length': 3},
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'password',
            'fullname',
            'bio',
            'profile_pic',
        )
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 5},
            'username': {'min_length': 3},
        }

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user
