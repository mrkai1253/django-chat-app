from django.urls import path
from .views import home, list_users, message_user

urlpatterns = [
    path('', home, name = 'home'),
    path('users/', list_users, name='users'),
    path('users/<username>', message_user, name='message-user'),
]
