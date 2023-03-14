from django.db import models

from users.models import User


class UserRegistrationLog(models.Model):
    # Usuário cujos dados são retirados da sessão
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='added_users')
    created_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='added_by_users')
    registration_date = models.DateTimeField(auto_now_add=True)
