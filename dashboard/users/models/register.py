from django.db import models
from .user import User


class UserRegistrationLog(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_user = models.ForeignKey(User, related_name='register', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.created_user
    
    
    