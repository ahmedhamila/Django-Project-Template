from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.users import USER_TYPE_CHOICES


class TemplateUser(AbstractUser):

    email = models.EmailField(
        _("email address"),
        blank=True,
        unique=True,
    )
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    image = models.ImageField(
        blank=True,
        null=True,
        upload_to="ProfileImages/",
    )
    phone_number = models.CharField(max_length=20, unique=True, null=True)
    user_type = models.CharField(
        max_length=200,
        choices=USER_TYPE_CHOICES,
        default=USER_TYPE_CHOICES[0][0],
    )

    groups = models.ManyToManyField(
        Group,
        related_name="groups_templateuser_set",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="user_permissions_templateuser_set",
        blank=True,
    )

    def __str__(self):
        return self.email

    @property
    def user_type_display(self):
        return self.user_type

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Template User"
        verbose_name_plural = "Template Users"
