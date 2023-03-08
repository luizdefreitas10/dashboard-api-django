from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from ..models import User
from ..serializers.register import UserRegisterSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserRegisterSerializer
    