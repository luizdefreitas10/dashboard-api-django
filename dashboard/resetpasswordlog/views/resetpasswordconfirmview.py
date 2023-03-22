from pyexpat.errors import messages
from django.contrib.auth import views as auth_views
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_decode
from ..models.resetpasswordlog import ResetPasswordLog
from django.utils import timezone

from users.models import User
# from django.contrib.auth.models import User

import logging 

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import SetPasswordForm

logger = logging.getLogger(__name__)


class ResetPasswordConfirmView(auth_views.PasswordResetConfirmView):
    
    def post(self, request, uidb64=None, token=None, *args, **kwargs):
        form = self.get_form()
        # token = request.GET.get('token')
        # print('token antes do form_valid', token)
        if form.is_valid():
            # Chamar o método reset_password_confirm para validar o token
            try:
                print('entrou')
                uid = urlsafe_base64_decode(uidb64).decode()
                print(uid)
                user = User.objects.get(pk=uid)
                print(user)
                print('este e o token', token)
                reset_log = ResetPasswordLog.objects.get(user=user, token=token)
                print('este e o resetlog', reset_log)
                reset_log.reset_password_confirm(request, uidb64, token, reset_log.expire_at)
                return super().post(request, uidb64=uidb64, token=token, *args, **kwargs)
            except (TypeError, ValueError, OverflowError, User.DoesNotExist, ResetPasswordLog.DoesNotExist):
                pass
        return super().post(request, uidb64=uidb64, token=token, *args, **kwargs)
    
    # def post(self, request, uidb64=None, token=None, *args, **kwargs):
    #     form = self.get_form()
    #     if form.is_valid():
    #         # print('asdsadasdasdasd',reset_log.token)
    #         # Chamar o método reset_password_confirm para validar o token
            
    #         try:
    #             uid = urlsafe_base64_decode(uidb64).decode()

    #             user = User.objects.get(pk=uid)

    #             reset_log = ResetPasswordLog.objects.get(pk=user.pk)

    #             if not reset_log.is_token_valid():
    #                 raise ValueError('Token expired or already used')
                    
    #             reset_log.reseted_at = timezone.now()
    #             reset_log.used_at = timezone.now()
    #             reset_log.status = 'reseted'
    #             reset_log.save()
    #             return super().post(request, uidb64=uidb64, token=token, *args, **kwargs)

    #         except (TypeError, ValueError, OverflowError, User.DoesNotExist, ResetPasswordLog.DoesNotExist):

    #             raise Http404('No reset password log found for the given user and token')
    #     return super().post(request, uidb64=uidb64, token=token, *args, **kwargs)
