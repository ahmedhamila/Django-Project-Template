from rest_framework_simplejwt.views import TokenObtainPairView

from src.users.serializers.TemplateUserObtainPairSerializer import PhoneTokenObtainPairSerializer
from src.users.serializers.TemplateUserObtainPairSerializer import TemplateUserObtainPairSerializer


class TemplateUserObtainPairView(TokenObtainPairView):
    serializer_class = TemplateUserObtainPairSerializer


class PhoneTokenObtainPairView(TokenObtainPairView):
    serializer_class = PhoneTokenObtainPairSerializer
