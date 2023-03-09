from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from accesslog.models.user_logs import UserAccessLog
from django.contrib import messages

# from users.models import User
from django.contrib.auth.models import User


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            UserAccessLog.objects.create(user=user, ip_address=request.META['REMOTE_ADDR'])
        
            return redirect('admin/')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        return render(request, 'registration/login.html')



# import jwt
# from django.shortcuts import render, redirect
# from django.conf import settings
# from django.contrib import messages
# from django.contrib.auth import authenticate
# from django.views.decorators.csrf import csrf_exempt


# @csrf_exempt
# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(username=username, password=password)

#         if user is not None:
#             payload = {
#                 'id': user.id,
#                 'username': user.username,
#             }

#             jwt_token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

#             request.session['jwt_token'] = jwt_token

#             return redirect('admin')
#         else:
#             messages.error(request, 'Invalid username or password')

#     return render(request, 'registration/login.html')


# from django.views.generic import View
# from django.http import HttpResponse


# from accesslog.models.user_logs import UserAccessLog

# # Create your views here.

# class UserAccessLogView(View):
    
# def login_view(self, request):
#         if request.user.is_authenticated:
#             UserAccessLog.objects.create(user=request.user, ip_address=request.META['REMOTE_ADDR'])
#         return HttpResponse(status=204)