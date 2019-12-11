from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token

from users.views import (
    RegisterUserView,
    UserView,
    UserProfileView,
    FollowUserView,
)

app_name = 'users'

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', obtain_jwt_token, name='login'),
    path('me/', UserView.as_view(), name='me'),
    path('<slug:username>/', UserProfileView.as_view(), name='user-profile'),
    path('<slug:username>/follow/', FollowUserView.as_view(), name='follow-user'),
]
