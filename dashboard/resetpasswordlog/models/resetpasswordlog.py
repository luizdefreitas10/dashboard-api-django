from django.db import models
# from django.contrib.auth.models import User
from users.models import User


# Create your models here.


class ResetPasswordLog(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    token = models.CharField(max_length=255)
    requested_at = models.DateTimeField(auto_now_add=True)
    reseted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, default='requested')
    