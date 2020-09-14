from rest_framework import serializers
from rest_framework.serializers import ValidationError
from .models import Todo


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title', 'description', 'done')


class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

    def validate_title(self, value):
        data = self.get_initial()
        title = data.get('title')

        if len(title) < 3:
            raise ValidationError("Title must be more than three")

        return value
