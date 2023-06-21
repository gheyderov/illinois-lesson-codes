from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from drf_yasg.utils import swagger_auto_schema
from accounts.api.serializers import UserProfileTokenSerializer

class LoginApiView(TokenObtainPairView):

    @swagger_auto_schema(responses={200: UserProfileTokenSerializer()})
    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)
