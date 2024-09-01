from django.contrib import admin

from src.example_app.models.Example import Example


class ExampleAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


admin.site.register(Example, ExampleAdmin)
