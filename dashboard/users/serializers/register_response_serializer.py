from rest_framework import serializers


class UserRegistrationResponseSerializer(serializers.Serializer):
    log_id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    created_username = serializers.CharField()
    created_by = serializers.CharField()