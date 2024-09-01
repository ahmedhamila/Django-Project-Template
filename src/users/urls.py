from django.urls import include
from django.urls import path

from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from src.users.controllers.TemplateUserViewSet import PhoneTokenObtainPairView
from src.users.controllers.TemplateUserViewSet import TemplateUserObtainPairView


router = routers.DefaultRouter()
urlpatterns = [
    path("", include(router.urls)),
    path(
        "login-email/",
        TemplateUserObtainPairView.as_view(),
        name="login-email",
    ),
    path(
        "login-phone/",
        PhoneTokenObtainPairView.as_view(),
        name="login-phone",
    ),
    path(
        "token-refresh/",
        TokenRefreshView.as_view(),
        name="token-refresh",
    ),
]
