from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes


from django.http import JsonResponse

from ..models.user_logs import UserAccessLog


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def all_user_access_logs(request):
    try:
        logs = UserAccessLog.objects.all()
        logs_data = [{'user_id': log.user.id, 'access_date': log.access_date, 'ip_address': log.ip_address} for log in logs]
        return JsonResponse({'success': True, 'logs': logs_data})
    except UserAccessLog.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'No access logs found'})
