from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

from simple_history.models import HistoricalRecords
from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
# Create your models here.

class User(AbstractUser):
    telefone = models.CharField(max_length=25)
    # history = HistoricalRecords(
    #     excluded_fields=['password', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'last_login', 'first_name', 'last_name', 'email', 'is_active', 'date_joined', 'telefone']
    # )
    history = AuditlogHistoryField()
    
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
    
    # def history_type_change(self):
    #     history_type_changed = self.history_type
    #     print(history_type_changed)

    # estudar sobre django signals para implementar corretamente a sobrescrita do metodo acima

auditlog.register(User)