from rest_framework import serializers

from src.example_app.models.Example import Example


class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = ["id", "title"]
