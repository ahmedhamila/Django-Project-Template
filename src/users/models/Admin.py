from django.contrib.auth.models import Permission
from django.db import models

from rest_framework import serializers

from src.users import PERMISSION_CODENAMES
from src.users.models.TemplateUser import TemplateUser
from src.utils.models import BaseModel


class Admin(BaseModel):
    super_user = models.BooleanField(default=False)
    user = models.OneToOneField(TemplateUser, on_delete=models.CASCADE)
    permissions = models.ManyToManyField(Permission, blank=True)

    def __str__(self):
        return self.user.email

    @property
    def permissions_list(self):
        return list(self.permissions.values_list("codename", flat=True))

    @property
    def is_supper_user(self):
        return self.super_user

    def set_permissions(self, rights):

        # Initialize sets for permissions to add and current permissions
        permissions_to_add = set()
        current_permissions = set(self.permissions.all())

        # Iterate through the provided rights to validate and collect permissions
        for right in rights:
            if right in PERMISSION_CODENAMES:
                for codename in PERMISSION_CODENAMES[right]["permissions"]:
                    try:
                        permission = Permission.objects.get(codename=codename)
                        permissions_to_add.add(permission)
                    except Permission.DoesNotExist:
                        raise serializers.ValidationError(
                            {
                                "permissions": [
                                    f"Permission with codename '{codename}' does not exist."
                                ]
                            }
                        )
            else:
                raise serializers.ValidationError({"rights": [f"Right '{right}' is not valid."]})

        # Determine permissions to remove
        permissions_to_remove = current_permissions - permissions_to_add

        # Update the permissions: add new ones and remove old ones
        self.permissions.remove(*permissions_to_remove)
        self.permissions.add(*permissions_to_add)

    def has_permission(self, perm):
        if self.super_user:
            return True
        return self.permissions.filter(codename=perm).exists()

    class Meta:
        verbose_name = "Admin"
        verbose_name_plural = "Admins"
