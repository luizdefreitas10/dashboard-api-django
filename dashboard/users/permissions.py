from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework.permissions import BasePermission
from rest_framework import permissions



class CanViewSet(BasePermission):
    def has_permission(self, request, view):
        # Verifica se o usuário atual pertence ao grupo Admin
        admin_group = Group.objects.get(name='Admin')
        return admin_group in request.user.groups.all()
    


class AllowResetPassword(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.__class__.__name__ == 'ResetPasswordView':
            return True
        return request.user.is_authenticated
    
    
class AllowAny(permissions.BasePermission):
    def has_permission(self, request, view):
        return True