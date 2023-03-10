from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.shortcuts import render
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.conf import settings
from django.core.mail import send_mail

from users.models import User
from ..models.resetpasswordlog import ResetPasswordLog

from django.contrib.auth.tokens import PasswordResetTokenGenerator

# Create your views here.


class ResetPasswordView(PasswordResetView):
    success_url = reverse_lazy('password_reset_done')

    def form_valid(self, form):
        response = super().form_valid(form)

        # Criar um registro no modelo ResetPasswordLog
        email = form.cleaned_data.get('email')
        user = User.objects.get(email=email)
        token_generator = PasswordResetTokenGenerator()
        token = token_generator.make_token(user)
        requested_at = timezone.now()
        status = 'requested'

        ResetPasswordLog.objects.create(
            user=user,
            token=token,
            requested_at=requested_at,
            status=status
        )

        return response