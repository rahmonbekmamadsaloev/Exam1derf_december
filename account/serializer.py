from .models import CustomUser
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    conf_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'password', 'conf_password']

    def validate(self, attrs):
        if attrs['password'] != attrs['conf_password']:
            raise serializers.ValidationError({'error': 'Пароли не совпадают'})
        return attrs

    def create(self, validated_data):
        validated_data.pop('conf_password')

        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
        )
        return user
    
    
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

