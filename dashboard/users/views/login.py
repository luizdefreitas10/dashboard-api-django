from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from ..serializers.login import LoginSerializer

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from ..permissions import CanViewSet

class LoginView(APIView):
    
    permission_classes = [IsAuthenticated, CanViewSet, IsAdminUser]
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )
        if user is None:
            return Response(
                {'error': 'Usuário ou senha inválidos.'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({'access_token': access_token})
