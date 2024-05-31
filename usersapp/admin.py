from django.contrib import admin

from usersapp.models import MyUsers, AuditLog, UsersLog, UserSession
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    list_display = ["id", "email", "first_name", "last_name", "is_staff", "phone"]
    fieldsets = [
        (None, {"fields": ["email", "first_name", "last_name", "password", "phone"]}),
        ("info", {"fields": ["last_login", "is_active"]}),
        ("Permissions", {"fields": ["is_staff", "is_superuser"]}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "first_name", "last_name", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email", "first_name", "last_name"]
    ordering = ["id"]


admin.site.register(MyUsers, UserAdmin)
admin.site.register(UserSession)


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'api', 'timestamp', 'status_code', 'success')
    list_filter = ('user', 'action', 'timestamp', 'success')
    search_fields = ('user__username', 'action', 'api')


class UserlogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'timestamp','changes', 'status_code', 'success')
#
#
admin.site.register(UsersLog, UserlogAdmin)
