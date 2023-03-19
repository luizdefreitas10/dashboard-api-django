from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, AbstractUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin

from simple_history.models import HistoricalRecords
from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog

# Create your models here.

class User(AbstractUser):
    telefone = models.CharField(max_length=25)
    
    use_in_migrations = True
    
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Users require an email field")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        
        self.password = make_password(self.password)
        
        return super().save(force_insert, force_update, using, update_fields)

    # estudar sobre django signals para implementar corretamente a sobrescrita do metodo acima

# class UserManager(BaseUserManager):
    
#     def create_user(self, email, username, password=None):
#         if not email:
#             raise ValueError('Users must have an email address')
        
#         user = self.model(
#             email=self.normalize_email(email),
#             username=username,
#         )
        
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, username, password):
#         user = self.create_user(
#             email=self.normalize_email(email),
#             username=username,
#             password=password,
#         )
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user

# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(max_length=255, unique=True)
#     username = models.CharField(max_length=255, unique=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     telefone = models.CharField(max_length=24)

#     objects = UserManager()

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']

#     def __str__(self):
#         return self.email



