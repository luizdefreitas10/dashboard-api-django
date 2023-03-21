from rest_framework import serializers

from ..models.user import User


class UserSerializer(serializers.ModelSerializer):
    created_username = serializers.CharField(max_length=255, read_only=True)
    
    class Meta:
        extra_kwargs = {
            "email": {"write_only": True},
        }
        model = User
        fields = (
            'id',
            'email',
            'password',
            'username',
            'first_name',
            'last_name',
            'telefone',
            'created_username',
        )
        
        def create(self, validated_data):
            return super().create(validated_data)
        
        def to_representation(self, instance):
            ret = super().to_representation(instance)
            ret['created_username'] = instance.username
            return ret