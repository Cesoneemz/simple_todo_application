from .models import Todo
from rest_framework import viewsets, permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TodoListSerializer, TodoCreateSerializer


class TodoListViewSet(generics.ListAPIView):
    queryset = Todo.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TodoListSerializer


class TodoCreateView(generics.CreateAPIView):
    serializer_class = TodoCreateSerializer


class Temp(APIView):

    def get(self, request, format=None):
        """Return dict with success message"""
        return Response({'message': 'success'})
