import datetime
import secrets
from django.db import models
from django.http import Http404
from django.shortcuts import render
from django.utils import timezone
from django.utils.http import urlsafe_base64_decode
# from django.contrib.auth.models import User
from users.models import User


# Create your models here.


class ResetPasswordLog(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    token = models.CharField(max_length=255)
    requested_at = models.DateTimeField(auto_now_add=True)
    reseted_at = models.DateTimeField(null=True, blank=True)
    used_at = models.DateTimeField(null=True, blank=True)
    expire_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.expire_at = timezone.now() + datetime.timedelta(hours=24)
            # self.used_at = None  # Define o campo used_at como nulo ao criar um novo objeto
        super().save(*args, **kwargs)
        
    
    def is_token_valid(self):
        now = timezone.now()
        if self.expire_at > now and self.used_at is None:
            return True
        else:
            return False
            
    
    
    def is_token_used(self):
        return self.used_at is not None
    
    
    def reset_password_confirm(self, request, uidb64, token, expire_at):
        try:
            print('executou')
            uid = urlsafe_base64_decode(uidb64).decode()
            print('este e o uid no model', uid)
            user = User.objects.get(pk=uid)
            print('este e o user no model', user)
            reset_log = ResetPasswordLog.objects.get(user=user, token=token)
            print('este e o reset log no model', reset_log)
            
            if not reset_log.is_token_valid():
                raise ValueError('Token expired')
            elif reset_log.used_at is not None:
                raise ValueError('Token already used')
            else:
                reset_log.reseted_at = timezone.now()
                reset_log.used_at = timezone.now()
                reset_log.status = 'reseted'
                reset_log.save()

        except (TypeError, ValueError, OverflowError, User.DoesNotExist, ResetPasswordLog.DoesNotExist):
            raise Http404('No reset password log found for the given user and token')
    
    
    def mark_token_as_used(self):
        self.used_at = timezone.now()
        self.status = 'reseted'
        self.save()
        