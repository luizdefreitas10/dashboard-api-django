from rest_framework import generics #importante o uso do genercis, pois facilita na escrita, e o get e post ja funcionamd por default
# from rest_framework.generics import get_object_or_404

from rest_framework import viewsets
# from rest_framework.decorators import action #alterar acoes dentro do model view
# from rest_framework.response import Response
# from rest_framework import mixins
# from rest_framework import permissions

from .models import User
from .serializers import UserSerializer


# Create your views here.

""" API v1 Users """

class UsersAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserAPIView(generics.RetrieveUpdateDestroyAPIView):    
    queryset = User.objects.all()
    serializer_class = UserSerializer

""" API v2 Users """

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer