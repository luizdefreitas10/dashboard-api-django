from django.db import models
from users.models.logdate import MixinsLogData
from users.validators import validate_phone


class Phone(MixinsLogData, models.Model):
    country_code = models.CharField(max_length=8, validators=[validate_phone])
    area_code = models.CharField(max_length=5, validators=[validate_phone])
    number = models.CharField(max_length=24, unique=True, validators=[validate_phone])

    @classmethod
    def self_create(cls, **kwargs):
        return cls.objects.create(**kwargs)

    def __str__(self) -> str:
        return f"{self.number}"