from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from src.users.serializers.TemplateUserObtainPairSerializer import PhoneTokenObtainPairSerializer
from src.users.serializers.TemplateUserObtainPairSerializer import TemplateUserObtainPairSerializer
from src.users.serializers.TemplateUserSignupSerializer import TemplateUserSignupSerializer


class TemplateUserObtainPairView(TokenObtainPairView):
    serializer_class = TemplateUserObtainPairSerializer


class PhoneTokenObtainPairView(TokenObtainPairView):
    serializer_class = PhoneTokenObtainPairSerializer


class TemplateUserSignupView(APIView):
    def post(self, request):
        serializer = TemplateUserSignupSerializer(data=request.data)
        if serializer.is_valid():
            user_data = serializer.save()
            return Response(user_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
