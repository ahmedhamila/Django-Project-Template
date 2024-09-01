from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from src.users.models.TemplateUser import TemplateUser
from src.users.serializers.TemplateUserSerializer import TemplateUserSerializer


class TemplateUserObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        return super().get_token(user)

    def validate(self, attrs):

        super().validate(attrs)
        refresh = self.get_token(self.user)
        access = refresh.access_token

        user_data = TemplateUserSerializer(self.user).data
        # TODO: can add conditional user_data based on usertype
        response_data = {
            "refresh": str(refresh),
            "access": str(access),
            "user": user_data,
        }

        return response_data


class PhoneTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = "phone_number"
    phone_number = serializers.CharField()

    def validate(self, attrs):
        phone_number = attrs.get("phone_number")
        password = attrs.get("password")

        user = TemplateUser.objects.filter(phone_number=phone_number).first()
        if user and user.check_password(password):
            attrs["email"] = user.email
            attrs.pop("phone_number")
            self.username_field = "email"
            super().validate(attrs)

            refresh = self.get_token(self.user)
            access = refresh.access_token

            user_data = TemplateUserSerializer(self.user).data

            return {
                "refresh": str(refresh),
                "access": str(access),
                "user": user_data,
            }
        raise serializers.ValidationError("Invalid credentials")

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token
