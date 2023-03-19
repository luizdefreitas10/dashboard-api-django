from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework.permissions import BasePermission



class CanViewSet(BasePermission):
    def has_permission(self, request, view):
        # Verifica se o usuário atual pertence ao grupo Admin
        admin_group = Group.objects.get(name='Admin')
        return admin_group in request.user.groups.all()