from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import Tag
from .models import Task


class Custom_User_admin(UserAdmin):
    model = User
    add_fieldsets = (*UserAdmin.add_fieldsets, ("Custom fields", {"fields": ("role",)}))
    fieldsets = (*UserAdmin.fieldsets, ("Custom field", {"fields": ("role",)}))


admin.site.register(User, Custom_User_admin)
admin.site.register(Tag)
admin.site.register(Task)
