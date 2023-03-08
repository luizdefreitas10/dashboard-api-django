from django.contrib import admin

# Register your models here.

from .models.user import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'password','first_name', 'last_name')