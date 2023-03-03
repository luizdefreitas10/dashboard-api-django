from django.contrib import admin

# Register your models here.

from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'password','first_name', 'last_name','telephone')