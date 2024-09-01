from rest_framework import serializers

from src.users.models.TemplateUser import TemplateUser


class TemplateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = TemplateUser
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "image",
            "user_type",
        ]
        read_only_fields = [
            "username",
        ]


class TemplateUserSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = TemplateUser
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone_number",
        ]
        extra_kwargs = {
            "email": {"required": True},
            "phone_number": {"required": True},
        }
