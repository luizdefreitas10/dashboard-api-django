from datetime import timezone
from rest_framework import serializers
from ..models import User
from ..models.register import UserRegistrationLog


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        
    def create(self, validated_data):
        return super().create(validated_data)