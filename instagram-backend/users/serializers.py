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
