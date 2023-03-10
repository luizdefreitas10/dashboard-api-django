from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect

from registerlog.models.registerlog import UserRegistrationLog
from ..models.registerlog import User
from django.contrib.auth import authenticate

from accesslog.utils.user_logs import log_user_access

from serializers.register_log import UserRegistrationLogSerializer


class CreateUserView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, ) 
    queryset = User.objects.all()
    serializer_class = UserRegistrationLogSerializer
    
    
    # Talvez essa sessão inteira de código (abaixo) seja totalmente 
    # inútil, pois so precisa enviar o dados + dados do user que criou
    # + dados da data em que foi criado algum usuário. -> o serializer faz isso
    def create_register_log(request):
        if request.user.is_authenticated:
            if request.method == 'POST':
                added_by = request.user.username
            
                username = request.POST['username']
                password = request.POST['password']
                email = request.POST['email']
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                telefone = request.POST['telefone']
                userLog = """ NÃO SEI OQUE VAI AQUI, SABOSTA!"""(request, 
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
                return render(request, 'templates/register.html')
        else:
            return messages.error(request, 'User not authenticated')
            
            
                
        # log_user_access(request)