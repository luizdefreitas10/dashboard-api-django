import datetime
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
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
        # response = super().form_valid(form)

        # Criar um registro no modelo ResetPasswordLog
        
        email = form.cleaned_data.get('email')
        user = User.objects.get(email=email)
        reset_log = ResetPasswordLog.objects.create(user=user)
        # print(dir(reset_log))
        
        # Gerar o token e armazená-lo no registro
        token_generator = PasswordResetTokenGenerator()
        token = token_generator.make_token(user)
        print(token)
        reset_log.token = token
        reset_log.requested_at = timezone.now()
        reset_log.save()
        
        # Enviar o email de redefinição de senha
        # reset_url = reverse('password_reset_confirm', kwargs={
        #     'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
        #     'token': reset_log.token,
        # })
        # reset_url = self.request.build_absolute_uri(reset_url)
        # reset_message = render_to_string('password_reset_email.html', {
        #     'user': user,
        #     'reset_url': reset_url,
        # })
        # send_mail('Reset Your Password', reset_message, 'noreply@example.com', [user.email])

   
        # Atualizar o registro do token
        
        # reset_log.reseted_at = timezone.now()
        # reset_log.used_at = timezone.now()
        # reset_log.status = 'reseted'
        # reset_log.save()

        return super().form_valid(form)