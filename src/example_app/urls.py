from django.urls import include
from django.urls import path

from rest_framework import routers

from src.example_app.controllers.ExampleViewSet import ExampleViewSet


router = routers.DefaultRouter()
router.register("example", ExampleViewSet)
urlpatterns = [
    path("", include(router.urls)),
]
