
from django.contrib import admin
from authapp import models



@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "email", "first_name", "last_name"]
    