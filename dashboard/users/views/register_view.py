from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from ..serializers.register import UserRegisterSerializer
from ..serializers.register_response_serializer import UserRegistrationResponseSerializer

from ..models.register import UserRegistrationLog


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    
    def create(self, request, *args, **kwargs):
        user_serializer = self.get_serializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        created_user = self.perform_create(user_serializer)
        
        # Assuming you have a method to create UserRegistrationLog and get the log_id
        created_log = self.create_user_registration_log(created_user, request.user)

        response_data = {
            'log_id': created_log.id,
            'user_id': created_user.id,
            'created_username': created_user.username,
            'created_by': request.user.username,
        }

        response_serializer = UserRegistrationResponseSerializer(data=response_data)
        response_serializer.is_valid(raise_exception=True)

        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        return serializer.save()

    def create_user_registration_log(self, created_user, created_by):
        log = UserRegistrationLog.objects.create(created_user=created_user, created_by=created_by)
        log.save()
        return log
    
    # def perform_create(self, serializer):
    #     serializer = UserRegisterSerializer(data=self.request.data)
    #     if not serializer.is_valid():
    #         raise ValidationError()
    #     serializer.save(is_superuser=True, is_staff=True)
    #     # cria o log de registro
    #     return Response(data=serializer.data, status=status.HTTP_201_CREATED)