from rest_framework import serializers
from ..models.registerlog import UserRegistrationLog

class UserRegistrationLogSerializer(serializers.ModelSerializer):
    model = UserRegistrationLog
    fields = ['id',
              'username'
              'password',
              'email', 
              'first_name',
              'last_name',
              'registration_date',
              'added_by']
    
    def create(self, validate_data):
        log = UserRegistrationLog.objects.create_user(**validate_data)
        # Os ** são desempacotadores de dicionário e passar seus valores como argumentos
        # para a função
        return log