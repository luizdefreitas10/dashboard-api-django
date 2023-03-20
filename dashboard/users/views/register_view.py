from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from rest_framework.exceptions import ValidationError

from ..models import User

from accesslog.utils.user_logs import log_user_access

from ..serializers.register import UserRegisterSerializer
from ..models.register import UserRegistrationLog


class CreateUserView(generics.CreateAPIView):
    # queryset = User.objects.all()
    # permission_classes = [IsAuthenticated]
    serializer_class = UserRegisterSerializer
    
    # def create_log(request):
    #     log_user_access(request)
    
    # pegar o usuario que esta sendo criado 
    # salvar no banco de dados os campos created_by, created_user e created_at
    
    # os dados vao vim do banco de dados 
    
    # sobrescrever o metodo post da view 
    
    def perform_create(self, serializer):
        serializer = UserRegisterSerializer(data=self.request.data)
        if not serializer.is_valid():
            raise ValidationError()
        serializer.save(is_superuser=True, is_staff=True)
        # cria o log de registro
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)