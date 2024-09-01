from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from src.users.models.TemplateUser import TemplateUser


class TemplateUserAdmin(UserAdmin):

    model = TemplateUser

    list_display = (
        "email",
        "username",
        "image",
        "phone_number",
        "user_type",
    )

    fieldsets = (
        (
            "User details",
            {
                "fields": (
                    "email",
                    "username",
                    "password",
                    "image",
                    "phone_number",
                    "user_type",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            "User Details",
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "image",
                    "user_type",
                    "phone_number",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )


admin.site.register(TemplateUser, TemplateUserAdmin)
