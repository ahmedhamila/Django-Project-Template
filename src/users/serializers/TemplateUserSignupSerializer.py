from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from src.users.models.TemplateUser import TemplateUser
from src.users.serializers.TemplateUserSerializer import TemplateUserSerializer


class TemplateUserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = TemplateUser
        fields = ["email", "password", "password_confirm"]
        # Add other fields as needed based on your TemplateUser model
        # e.g., fields = ['email', 'first_name', 'last_name', 'phone_number', 'password',
        #  'password_confirm']

    def validate(self, attrs):
        password = attrs.get("password")
        password_confirm = attrs.pop("password_confirm", None)

        if password != password_confirm:
            raise serializers.ValidationError("Passwords do not match")

        return attrs

    def validate_email(self, value):
        if TemplateUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value

    def create(self, validated_data):
        # Create user
        user = TemplateUser.objects.create_user(**validated_data, username=validated_data["email"])

        # Generate tokens
        refresh = RefreshToken.for_user(user)
        access = refresh.access_token

        # Serialize user data
        user_data = TemplateUserSerializer(user).data

        return {
            "refresh": str(refresh),
            "access": str(access),
            "user": user_data,
        }
