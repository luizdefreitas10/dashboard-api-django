from rest_framework.exceptions import ValidationError


def validate_phone(value: str):
    if not value.isdigit():
        raise ValidationError(detail="Número inválido")