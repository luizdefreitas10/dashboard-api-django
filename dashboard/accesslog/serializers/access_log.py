from rest_framework import serializers
from ..models.user_logs import UserAccessLog


class UserAccessLogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserAccessLog
        fields = ['id', 'user', 'access_date', 'ip_address']
        
        def create(self, validated_data):
            log = UserAccessLog.objects.create_user(**validated_data)
            return log