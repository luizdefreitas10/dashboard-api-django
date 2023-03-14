from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect

# from dashboard.accesslog.models.user_logs import UserRegistrationLog
from ..models import User
from django.contrib.auth import authenticate

from accesslog.utils.user_logs import log_user_access

from ..serializers.register import UserRegisterSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserRegisterSerializer