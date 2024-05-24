from django.contrib import admin

from user.models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    last_display = ("id", "email")
