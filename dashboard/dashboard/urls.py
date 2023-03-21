"""
dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from django.contrib import admin
from django.urls import path, include
from users.urls import router

from users.views.logoutview import logout
from users.views.login import LoginView

from resetpasswordlog.views.resetpasswordview import ResetPasswordView

from resetpasswordlog.views.resetpasswordconfirmview import ResetPasswordConfirmView

from accesslog.views.access_logs_view import user_access_logs
from accesslog.views.all_access_logs_view import all_user_access_logs

from users.views.api_register_log_view import create_user_with_log

from users.views.api_register_logs import UserRegistrationLogList, UserRegistrationLogDetail

from resetpasswordlog.views.resetpassword_api import ResetPasswordLogList

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    #API de retorno de ususarios, CRUD: 
    path('api/v1/', include("users.urls")),
    path('api/v2/', include(router.urls)),
    
    # API de login:
    path('admin/', admin.site.urls),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', logout, name='logout'),
    
    # API para trazer os logs de acesso de usuarios: 
    path('api/users/access-logs/', all_user_access_logs, name='all_user_access_logs'),
    path('api/users/<int:user_id>/access-logs/', user_access_logs, name='user_access_logs'),
    
    #TOKEN resrefh: 
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    # API para reset de password: 
    path('reset_password/', ResetPasswordView.as_view(), name='reset_password'),
    path('reset_password/<uidb64>/<token>/', csrf_exempt(ResetPasswordConfirmView.as_view()), name='password_reset_confirm'),
    
    #API log de redefinicao de senha:
    path('api/password-reset-logs/', ResetPasswordLogList.as_view(), name='password_reset_logs'),
    
    # path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    #API para registro de novos usuarios: 

    path('api/auth/register/', create_user_with_log, name='create_user_with_log'),
    
    #API para retorno dos logs de cadastros: 
    path('api/registration-logs/', UserRegistrationLogList.as_view(), name='user_registration_logs'),
    path('api/registration-logs/<int:user_id>/', UserRegistrationLogDetail.as_view(), name='user_registration_logs_by_user_id'),
]

