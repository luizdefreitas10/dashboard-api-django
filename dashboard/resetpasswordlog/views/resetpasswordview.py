from django.utils import timezone

from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.conf import settings
from django.core.mail import send_mail

from users.models import User

from ..serializers.resetlogserializer import ResetPasswordLogSerializer

from ..models.resetpasswordlog import ResetPasswordLog

from django.contrib.auth.tokens import PasswordResetTokenGenerator

from rest_framework.response import Response

from rest_framework.views import APIView
from users.permissions import AllowAny

from django.core.exceptions import ValidationError
from django.core.validators import validate_email

# Create your views here.


class ResetPasswordView(APIView):
    permission_classes = [AllowAny]
    # serializer_class = ResetPasswordLogSerializer
    
    def post(self, request):
        # serializer = ResetPasswordLogSerializer(data=request.data)
        email = request.data.get("email")
        
        if not email:
            return Response({"detail": "E-mail é obrigatório."}, status=400)

        try:
            validate_email(email)
        except ValidationError:
            return Response({"detail": "E-mail inválido."}, status=400)
            
        try:
            # serializer.save()
            user: User = User.get_user_by_email(email)

            # Criar um registro no modelo ResetPasswordLog
            reset_log = ResetPasswordLog.objects.create(user=user)

            # Gerar o token e armazená-lo no registro
            token_generator = PasswordResetTokenGenerator()
            token = token_generator.make_token(user)
            reset_log.token = token
            reset_log.requested_at = timezone.now()
            reset_log.save()

            # Enviar o e-mail de redefinição de senha
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            reset_url = f"https://localhost:3000/reset_password/{uidb64}/{token}/"
            subject = "Redefinição de senha"
            message = f"""Olá {user.first_name},

Você solicitou a redefinição da sua senha. Por favor, clique no link abaixo para redefinir sua senha:

{reset_url}

Este é o uid do seu usuario, caso necessite: {uidb64}
Este é o token de redefinição de senha: {token}


Se você não solicitou a redefinição de senha, por favor, ignore este e-mail.

Atenciosamente,
Equipe Gds Tec"""

            from_email = "noreply@example.com"
            to_email = [user.email]
            send_mail(subject, message, from_email, to_email)

            return Response({"detail": "E-mail de redefinição de senha enviado com sucesso."}, status=201)
            
        except User.DoesNotExist:
                return Response({"detail": "E-mail não encontrado"}, status=400)
            
        # else:
        #     return Response(serializer.errors, status=400)
    

    