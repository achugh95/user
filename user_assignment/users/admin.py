from django.contrib import admin
from user_assignment.users.models import MyUser

# Register your models here.

class UserAdmin(admin.ModelAdmin):

    list_display        = ("id", "username", "is_staff", "is_superuser")

admin.site.register(MyUser, UserAdmin)

