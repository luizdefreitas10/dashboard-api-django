from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect

from dashboard.accesslog.models.user_logs import UserRegistrationLog
from ..models import User
from django.contrib.auth import authenticate

from accesslog.utils.user_logs import log_user_access

from ..serializers.register import UserRegisterSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserRegisterSerializer
    
    def create_register_log(request):
        if request.user.is_authenticated:
            if request.method == 'POST':
                added_by = request.user
            
                username = request.POST['username']
                password = request.POST['password']
                email = request.POST['email']
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                telefone = request.POST['telefone']
                userLog = is_valid(request, 
                                    username=username,
                                    password=password, 
                                    email=email,
                                    first_name=first_name,
                                    last_name=last_name,
                                    telefone=telefone,
                                    added_by=added_by)

                if userLog is not None:
                    UserRegistrationLog.objects.create(user=userLog)
                    
                    return HttpResponseRedirect('login/')
                else:
                    messages.error(request, 'All obligatory fields must be filled.')
            else:
                return render(request, 'registration/register.html')
            
            
                
        log_user_access(request)