from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from ..models import User

from accesslog.utils.user_logs import log_user_access

from ..serializers.register import UserRegisterSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserRegisterSerializer
    
    # def create_log(request):
    #     log_user_access(request)