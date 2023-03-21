from rest_framework.generics import ListAPIView

from ..models.resetpasswordlog import ResetPasswordLog

from ..serializers.resetlogserializer import ResetPasswordLogSerializer


class ResetPasswordLogList(ListAPIView):
    queryset = ResetPasswordLog.objects.all()
    serializer_class = ResetPasswordLogSerializer
