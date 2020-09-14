from rest_framework import routers
from django.urls import path, include
from .views import TodoListViewSet, TodoCreateView

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


urlpatterns = [
    path('', TodoListViewSet.as_view()),
    path('create/', TodoCreateView.as_view()),
    path('auth/', obtain_jwt_token),
    path('auth-refresh/', refresh_jwt_token)
]