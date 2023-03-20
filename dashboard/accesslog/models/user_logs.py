from django.db import models

# from django.contrib.auth.models import User

from users.models import User

# Create your models here.

class UserAccessLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='access_log')
    access_date = models.DateTimeField(auto_now_add=True)
    ip_address = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.user.username