from ..models import UserAccessLog


def log_user_access(request):
        if request.user.is_authenticated:
            # Registro de log de acesso do usuário
            UserAccessLog.objects.create(user=request.user, ip_address=request.META['REMOTE_ADDR'])