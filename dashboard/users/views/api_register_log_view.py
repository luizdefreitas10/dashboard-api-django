from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from datetime import datetime, timezone
# from .models import User, UserRegistrationLog
from ..models.user import User
from ..models.register import UserRegistrationLog


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_user_with_log(request):
    # Verifique se o usuário atual é um administrador
    if not request.user.is_staff:
        return JsonResponse({'success': False, 'error': 'Only admins can create new users.'})

    # Extraia os dados do usuário do corpo da solicitação
    email = request.data.get('email')
    password = request.data.get('password')
    telefone = request.data.get('telefone')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    username = request.data.get('username')

    # Crie o novo usuário
    new_user = User.objects.create_user(username=username, email=email, password=password, telefone=telefone, first_name=first_name, last_name=last_name, is_superuser=True, is_staff=True, is_active=True)
    print(new_user)

    # Registre o log de registro
    registration_log = UserRegistrationLog.objects.create(
        created_by=request.user,
        created_user=new_user,
        created_at=datetime.now(timezone.utc)
    ) 
    # print(registration_log)
    #resposta json: 
    response_data = {
        'created_by': request.user.username,  # Use o atributo 'username' em vez do objeto User
        'user_id': new_user.id,
        'log_id': registration_log.id,
        'created_username': new_user.username,
    }

    return JsonResponse(response_data)

