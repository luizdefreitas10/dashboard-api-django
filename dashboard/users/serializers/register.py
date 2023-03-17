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
        user = User.objects.create_user(**validated_data)
        
        # Criar o registro de log
        # request = self.context.get('request')
        # if request and request.user.is_authenticated:
        #     log_data = {
        #         'created_by': request.user,
        #         'created_user': user,
        #         'created_at': timezone.now()
        #     }
        #     UserRegistrationLog.objects.create(**log_data)
            
        return user