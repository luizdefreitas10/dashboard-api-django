from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import (
    UserViewSet,
    UsersAPIView,
    UserAPIView,
    )


router = SimpleRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('users/', UsersAPIView.as_view(), name='users'),
    path('users/<int:pk>', UserAPIView.as_view(), name='user')
]
