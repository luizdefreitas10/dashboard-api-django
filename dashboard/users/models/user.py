from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.contrib.auth.hashers import make_password

from users.models.logdate import MixinsLogData

# Create your models here.

class User(AbstractUser):
    telefone = models.CharField(max_length=25)
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None) -> None:
        self.password = make_password(self.password)
        return super().save(force_insert, force_update, using, update_fields)
    
    # estudar sobre django signals para implementar corretamente a sobrescrita do metodo acima
     
# class Base(models.Model):
#     criacao = models.DateTimeField(auto_now_add=True)
#     atualizacao = models.DateTimeField(auto_now=True)
#     ativo = models.BooleanField(default=True)

#     class Meta:
#         abstract = True

# class User(Base):
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=20)
#     username = models.CharField(max_length=100, unique=True)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     telephone = models.CharField(max_length=24, unique=True)
    
#     class Meta:
#         verbose_name = "User"
#         verbose_name_plural = "Users"
#         unique_together = ('email', 'username', 'telephone')
    
    
#     def __str__(self):
#         return self.username

    
# class UserAccessLog(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='access_log')
#     access_date = models.DateTimeField(auto_now_add=True)
#     ip_address = models.GenericIPAddressField()
    
    
# class UserRegistrationLog(models.Model):
#     added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='added_users')
#     new_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='added_by_users')
#     registration_date = models.DateTimeField(auto_now_add=True)
    

# class PasswordResetLog(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='password_reset_log')
#     reset_date = models.DateTimeField(auto_now_add=True)

