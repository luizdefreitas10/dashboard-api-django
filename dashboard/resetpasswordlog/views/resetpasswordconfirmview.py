from django.contrib.auth import views as auth_views
from django.utils.http import urlsafe_base64_decode
from ..models.resetpasswordlog import ResetPasswordLog

from users.models import User


class ResetPasswordConfirmView(auth_views.PasswordResetConfirmView):
    def post(self, request, uidb64=None, token=None, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            # Chamar o método reset_password_confirm para validar o token
            try:
                uid = urlsafe_base64_decode(uidb64).decode()
                user = User.objects.get(pk=uid)
                reset_log = ResetPasswordLog.objects.get(user=user, token=token)
                reset_log.reset_password_confirm(request, uidb64, token, reset_log.expire_at)
                return super().post(request, uidb64=uidb64, token=token, *args, **kwargs)
            except (TypeError, ValueError, OverflowError, User.DoesNotExist, ResetPasswordLog.DoesNotExist):
                pass
        return super().post(request, uidb64=uidb64, token=token, *args, **kwargs)