from rest_framework import serializers
from .models import Course, CourseModule, Task

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'

    def validate_max_score(self, value):
        if value <= 0:
            raise serializers.ValidationError('max_score должен быть > 0')
        return value


class CourseModuleSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = CourseModule
        fields = ['id', 'title', 'order', 'tasks']


class CourseSerializer(serializers.ModelSerializer):
    modules = CourseModuleSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'modules']
