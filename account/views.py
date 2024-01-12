from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from .models import User
from rest_framework import permissions
from .serializers import UserSerializer, GoogleSocialAuthSerializer
import utils.response_handler as rh
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Create your views here.


class LoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer_data = self.get_serializer(data=request.data)
        serializer_data.is_valid(raise_exception=True)
        response = rh.ResponseMsg(
            serializer_data.validated_data, False, "Login Successfully!!!"
        )
        return Response(status=status.HTTP_200_OK, data=response.response)


class RefreshTokenView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        serializer_data = super().post(request, *args, **kwargs)
        response = rh.ResponseMsg(
            serializer_data.data,
            False,
            "Access Token Get Successfully!!!",
        )
        return Response(status=status.HTTP_200_OK, data=response.response)


class UserManagerView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer


class GoogleSocialAuthView(generics.GenericAPIView):
    serializer_class = GoogleSocialAuthSerializer

    def post(self, request):
        """

        POST with "auth_token"

        Send an idtoken as from google to get user information

        """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        response = rh.ResponseMsg(data, False, "Login Successfully!!!")
        return Response(status=status.HTTP_200_OK, data=response.response)
