from django.db import models

from .user_logs import User

# Create your models here.

class UserAccessLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='access_log')
    access_date = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()
    
    
class UserRegistrationLog(models.Model):
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='added_users')
    new_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='added_by_users')
    registration_date = models.DateTimeField(auto_now_add=True)
    

class PasswordResetLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='password_reset_log')
    reset_date = models.DateTimeField(auto_now_add=True)