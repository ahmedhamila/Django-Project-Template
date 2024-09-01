from django.contrib import admin

from src.users.models.Admin import Admin


class AdminAdmin(admin.ModelAdmin):
    model = Admin


admin.site.register(Admin, AdminAdmin)
