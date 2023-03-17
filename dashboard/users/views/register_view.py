from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from ..models import User

from accesslog.utils.user_logs import log_user_access

from ..serializers.register import UserRegisterSerializer
from ..models.register import UserRegistrationLog


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserRegisterSerializer
    
    # def create_log(request):
    #     log_user_access(request)
    
    # pegar o usuario que esta sendo criado 
    # salvar no banco de dados os campos created_by, created_user e created_at
    
    # os dados vao vim do banco de dados 
    
    # sobrescrever o metodo post da view 
    
    def perform_create(self, serializer):
        
        # pegar o usuario que esta logado, autenticado e criando o novo usuario
        user = self.request.user
        # print('usuario do self.request.user', user)
        
        # cria o usuário
        serializer.save()
        
        # pega o usuário criado
        created_user = serializer.instance
        # print('created_user is ', created_user)
        
        # cria o log de registro
        UserRegistrationLog.objects.create(
            created_by = user,
            created_user = created_user
        )
        
        # retorna a resposta padrão da criação
        return Response(serializer.data, status=status.HTTP_201_CREATED)