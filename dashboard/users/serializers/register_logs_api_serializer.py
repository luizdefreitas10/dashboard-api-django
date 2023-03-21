from rest_framework import serializers
# from .models import UserRegistrationLog
from ..models.register import UserRegistrationLog

class UserRegistrationLogSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    created_user = serializers.StringRelatedField()

    class Meta:
        model = UserRegistrationLog
        fields = ('id', 'created_by', 'created_user', 'created_at')