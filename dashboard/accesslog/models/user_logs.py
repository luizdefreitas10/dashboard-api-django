from django.db import models

# from django.contrib.auth.models import User

from users.models import User

# Create your models here.

class UserAccessLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='access_log')
    access_date = models.DateTimeField(auto_now_add=True)
    ip_address = models.CharField(max_length=255, blank=True, null=True)
    

class PasswordResetLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='password_reset_log')
    reset_date = models.DateTimeField(auto_now_add=True)