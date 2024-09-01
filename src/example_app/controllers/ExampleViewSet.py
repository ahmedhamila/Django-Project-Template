from rest_framework import viewsets

from src.example_app.models.Example import Example
from src.example_app.serializers.ExampleSerializer import ExampleSerializer


class ExampleViewSet(viewsets.ModelViewSet):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer
