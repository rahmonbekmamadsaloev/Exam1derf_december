from rest_framework import serializers
from .models import Submission

class SubmissionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Submission
        fields = '__all__'
        read_only_fields = ['status']

    def validate(self, attrs):
        task = attrs.get('task')
        score = attrs.get('score', 0)

        if not task.is_active:
            raise serializers.ValidationError('Задача не активна')

        if score > task.max_score:
            raise serializers.ValidationError('score превышает max_score')

        return attrs

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['username'] = instance.user.username
        data['task'] = instance.task.title
        data['module'] = instance.task.module.title
        data['course'] = instance.task.module.course.title
        return data
