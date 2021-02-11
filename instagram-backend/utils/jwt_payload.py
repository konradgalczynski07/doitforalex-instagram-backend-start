from datetime import datetime

from rest_framework_jwt.settings import api_settings


def jwt_payload_handler(user):
    """Slightly customized jwt payload that include user profile picture"""

    payload = {
        'user_id': user.pk,
        'username': user.username,
        'fullname': user.fullname,
        'profile_pic': user.profile_pic.url,
        'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA,
    }

    return payload
