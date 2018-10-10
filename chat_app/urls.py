from django.urls import path
from .views import home, list_users, message_user,login_func

urlpatterns = [
    path('', home, name = 'home'),
    path('login/',login_func,name = 'login'),
    path('users/', list_users, name='users'),
    path('users/<username>', message_user, name='message-user'),
]
