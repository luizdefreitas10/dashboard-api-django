from django.db import models

# Create your models here.

class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

class User(Base):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=24, unique=True)
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        unique_together = ('email', 'username', 'telephone')
    
    
    def __str__(self):
        return self.username