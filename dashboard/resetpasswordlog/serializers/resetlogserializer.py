from rest_framework import serializers
from ..models.resetpasswordlog import ResetPasswordLog


class ResetPasswordLogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ResetPasswordLog
        fields = ['id', 'token', 'requested_at', 'reseted_at', 'status', 'user_id', 'expire_at', 'used_at']
        
        