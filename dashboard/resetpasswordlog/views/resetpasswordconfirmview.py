from django.contrib.auth import views as auth_views
from django.http import Http404
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_decode
from ..models.resetpasswordlog import ResetPasswordLog
from django.utils import timezone

from users.models import User
# from django.contrib.auth.models import User

import logging 

from django.contrib.auth.tokens import PasswordResetTokenGenerator

logger = logging.getLogger(__name__)


class ResetPasswordConfirmView(auth_views.PasswordResetConfirmView):
    
    def post(self, request, uidb64=None, token=None, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            # print('asdsadasdasdasd',reset_log.token)
            # Chamar o método reset_password_confirm para validar o token
            
            try:
                # print('PRITANDO A CLASSE', auth_views.PasswordResetConfirmView.reset_url_token)
                # user_token = ResetPasswordLog.objects.get(token=token)
                # print(user_token)
                print("entrei no if")
                uid = urlsafe_base64_decode(uidb64).decode()
                user = User.objects.get(pk=uid)
                print(user.pk)
                reset_log: ResetPasswordLog = ResetPasswordLog.objects.filter(id=user.pk, token=token)
                reset_lo2g= ResetPasswordLog.objects.filter(user=user, token=token).last()
                print(reset_log)
                print(reset_lo2g)
                reset_log.is_token_valid()
                reset_log.reseted_at = timezone.now()
                reset_log.used_at = timezone.now()
                reset_log.status = 'reseted'
                reset_log.save()
                return super().post(request, uidb64=uidb64, token=token, *args, **kwargs)

            except (TypeError, ValueError, OverflowError, User.DoesNotExist, ResetPasswordLog.DoesNotExist):

                raise Http404('No reset password log found for the given user and token')
        return super().post(request, uidb64=uidb64, token=token, *args, **kwargs)
    