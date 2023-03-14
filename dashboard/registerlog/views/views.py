from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect
from registerlog.models.registerlog import UserRegistrationLog
from ..models.registerlog import User
from django.contrib.auth import authenticate
from accesslog.utils.user_logs import log_user_access
from ..serializers.register_log import UserRegistrationLogSerializer
from ..models.registerlog import UserRegistrationLog


from rest_framework import serializers, views, status
from rest_framework.response import Response
class UserCreationView(views.APIView):
    serializer_class = UserRegistrationLogSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # create a new user
            user = User.objects.create_user(**serializer.validated_data)
            # save information about the user creation action
            UserRegistrationLog.objects.create(
                created_by=request.user,
                added_by=request.user.username, # new field
                created_user=user,
            )

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
 
 
 
 
    # permission_classes = (IsAuthenticated, ) 
    # queryset = User.objects.all()
    # serializer_class = UserRegistrationLogSerializer
    
    
    # # Talvez essa sessão inteira de código (abaixo) seja totalmente 
    # # inútil, pois so precisa enviar o dados + dados do user que criou
    # # + dados da data em que foi criado algum usuário. -> o serializer faz isso
    # def create_register_log(request):
    #     # if request.user.is_authenticated:
    #         if request.method == 'POST':
    #             added_by = request.user.username
            
    #             username = request.POST['username']
    #             password = request.POST['password']
    #             email = request.POST['email']
    #             first_name = request.POST['first_name']
    #             last_name = request.POST['last_name']
    #             telefone = request.POST['telefone']
    #             userLog = authenticate(request, 
    #                     username=username,
    #                     password=password, 
    #                     email=email,
    #                     first_name=first_name,
    #                     last_name=last_name,
    #                     telefone=telefone,
    #                     added_by=added_by)

    #             if userLog is not None:
    #                 UserRegistrationLog.objects.create(user=userLog)
                    
    #                 return HttpResponseRedirect('login/')
    #             else:
    #                 messages.error(request, 'All obligatory fields must be filled.')
    #         else:
    #             return render(request, 'templates/register.html')
    #     # else:
    #     #     return messages.error(request, 'User not authenticated')
            
            
                
        # log_user_access(request)