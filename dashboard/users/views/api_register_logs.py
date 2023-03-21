from rest_framework import generics
# from .models import UserRegistrationLog
from ..models.register import UserRegistrationLog
from ..serializers.register_logs_api_serializer import UserRegistrationLogSerializer

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class UserRegistrationLogList(generics.ListAPIView):
    queryset = UserRegistrationLog.objects.all()
    serializer_class = UserRegistrationLogSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class UserRegistrationLogDetail(generics.ListAPIView):
    serializer_class = UserRegistrationLogSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return UserRegistrationLog.objects.filter(created_by__id=user_id)
