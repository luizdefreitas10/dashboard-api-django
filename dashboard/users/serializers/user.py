from rest_framework import serializers

from ..models.user import User


class UserSerializer(serializers.ModelSerializer):
    
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
        )