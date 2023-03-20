from datetime import datetime, timezone
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from accesslog.models.user_logs import UserAccessLog
from rest_framework_simplejwt.tokens import AccessToken
from users.models.user import User

class LoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
    
    def get_queryset(self):
        return User.objects.all()
    
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        # se o login for bem-sucedido, o token de acesso será retornado na resposta
        if response.status_code == status.HTTP_200_OK:
            # decodificar o token de acesso para obter as informações do usuário
            access_token = response.data["access"]
            decoded_token = AccessToken(access_token)
            user_id = decoded_token['user_id']
            user = self.get_queryset().get(pk=user_id)
            # salvar os dados de acesso do usuário no banco de dados
            access_log = UserAccessLog.objects.create(
                user=user,
                access_date=datetime.now(timezone.utc),
                ip_address=request.META.get('REMOTE_ADDR')
            )
            access_log.save()
        return response

    def get_user_by_token(self, access_token):
        """
        Retorna o objeto do usuário a partir do token de acesso.
        """
        decoded_payload = self.get_token_decoder()(access_token)
        user_id = decoded_payload['user_id']
        return self.get_queryset().get(pk=user_id)
    
    def get_token_decoder(self):
        """
        Retorna a função de decodificação de token.
        """
        return self.get_serializer().get_token_decoder()



# class LoginView(APIView):
    
#     permission_classes = [IsAuthenticated, CanViewSet, IsAdminUser]
    
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = authenticate(
#             email=serializer.validated_data['email'],
#             password=serializer.validated_data['password']
#         )
#         if user is None:
#             return Response(
#                 {'error': 'Usuário ou senha inválidos.'},
#                 status=status.HTTP_401_UNAUTHORIZED
#             )

#         refresh = RefreshToken.for_user(user)
#         access_token = str(refresh.access_token)

#         return Response({'access_token': access_token})
