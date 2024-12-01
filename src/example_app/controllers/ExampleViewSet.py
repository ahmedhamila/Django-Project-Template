from rest_framework import viewsets

from src.example_app.models.Example import Example
from src.example_app.serializers.ExampleSerializer import ExampleSerializer
from src.utils.pagination import PaginationClass


class ExampleViewSet(viewsets.ModelViewSet):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer
    pagination_class = PaginationClass
