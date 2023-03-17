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

from users.views.register_view import CreateUserView

from accesslog.views.logoutview import logout
from accesslog.views.loginview import LoginView

from resetpasswordlog.views.resetpasswordview import ResetPasswordView

from resetpasswordlog.views.resetpasswordconfirmview import ResetPasswordConfirmView

# from ..accesslog.views.access_logs_view import login


urlpatterns = [
    
    path('api/v1/', include("users.urls")),
    path('api/v2/', include(router.urls)),
    
    path('admin/', admin.site.urls),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', logout, name='logout'),
    
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    path('reset_password/', ResetPasswordView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset_password/<uidb64>/<token>/', ResetPasswordConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset_password/<uidb64>/', ResetPasswordConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    path('api/auth/register/', CreateUserView.as_view(), name='register'),
    
]
