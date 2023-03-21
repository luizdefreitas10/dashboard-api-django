from datetime import timezone
from rest_framework import serializers
from ..models import User
from ..models.register import UserRegistrationLog


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    created_username = serializers.CharField(read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'created_username']
        
    def create(self, validated_data):
        return super().create(validated_data)
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['created_username'] = instance.username
        return ret