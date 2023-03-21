
from django.contrib.auth import views as auth_views

from django.utils.http import urlsafe_base64_decode
from ..models.resetpasswordlog import ResetPasswordLog

from django.utils.encoding import force_str
from rest_framework.response import Response

from users.models import User


from django.utils.http import urlsafe_base64_decode


class ResetPasswordConfirmView(auth_views.PasswordResetConfirmView):
    
    def post(self, request, uidb64, token):
        # Decodificar o UID e obter o usuário
        uid = force_str(urlsafe_base64_decode(uidb64))
        try:
            user = User.objects.get(pk=uid)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

        # Obter o log de redefinição de senha
        try:
            reset_log = ResetPasswordLog.objects.get(user=user, token=token)
        except ResetPasswordLog.DoesNotExist:
            return Response({"error": "Invalid token"}, status=400)

        # Verificar se o token é válido e não expirado
        if not reset_log.is_token_valid():
            return Response({"error": "Token expired or already used"}, status=400)

        # Redefinir a senha
        new_password = request.data.get('new_password')
        confirm_password = request.data.get('confirm_password')

        if new_password != confirm_password:
            return Response({"error": "Passwords do not match"}, status=400)

        user.set_password(new_password)
        user.save()

        # Marcar o token como usado
        reset_log.mark_token_as_used()

        return Response({"message": "Password reset successfully"}, status=200)