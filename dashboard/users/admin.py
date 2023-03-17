from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

from .models.user import User
from .models.register import UserRegistrationLog

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'username', 'password','first_name', 'last_name')
    
    def save_model(self, request, obj, form, change):
        # Get the current user
        created_by = request.user
        
        # Save the user and get the created user
        created_user = super().save_model(request, obj, form, change)
        
        # Create the log entry
        UserRegistrationLog.objects.create(created_by=created_by, created_user=created_user)
        
        return created_user


class UserRegistrationLogAdmin(admin.ModelAdmin):
    list_display = ('created_by', 'created_user', 'created_at')

class CustomUserAdmin(UserAdmin):
    def save_model(self, request, obj, form, change):
        # Get the current user
        created_by = request.user
        
        # Save the user and get the created user
        created_user = super().save_model(request, obj, form, change)
        
        # Create the log entry
        UserRegistrationLog.objects.create(created_by=created_by, created_user=created_user)
        
        return created_user

# Set the new UserAdmin as the admin for User model
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Register UserRegistrationLogAdmin as admin for UserRegistrationLog model
admin.site.register(UserRegistrationLog, UserRegistrationLogAdmin)



# class UserRegistrationLogForm(forms.ModelForm):
#     class Meta:
#         model = UserRegistrationLog
#         fields = "__all__"

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['created_user'].widget = forms.HiddenInput()
#         self.fields['created_user'].initial = self.instance.created_user    
    

# class UserRegistrationLogAdmin(admin.ModelAdmin):
#     def save_model(self, request, obj, form, change):
#         # Get the current user
#         created_by = request.user
#         print('created_by', created_by)
        
#         # Save the user and get the created user
#         created_user = super().save_model(request, obj, form, change)
#         print('created_user', created_user)
        
#         # Create the log entry
#         UserRegistrationLog.objects.create(created_by=created_by, created_user=created_user)
        
#         return created_user
    
        
admin.site.unregister(User)
admin.site.register(User, UserAdmin)