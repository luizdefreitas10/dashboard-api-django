from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

from django.contrib.auth.models import User

# from .user_logs import User

# Create your models here.

User = get_user_model()

class UserAccessLog(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='access_log')
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    access_date = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()
    
    
class UserRegistrationLog(models.Model):
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='added_users')
    new_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='added_by_users')
    registration_date = models.DateTimeField(auto_now_add=True)
    

class PasswordResetLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='password_reset_log')
    reset_date = models.DateTimeField(auto_now_add=True)