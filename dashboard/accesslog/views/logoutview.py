from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def logout(request):
    try:
        print('entrei no try')
        refresh_token = request.data["refresh_token"]
        print(refresh_token)
        token = RefreshToken(refresh_token)
        print(token)
        token.blacklist()
        return Response(status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        error = dict(message='Falha ao efetuar o logout', status=status.HTTP_400_BAD_REQUEST)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)