from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

# Register your models here.


class CustomUserAdmin(UserAdmin):
    readonly_fields = (
        "date_joined",
        "last_login",
        "updated_at",
    )

    fieldsets = (
        (
            "Credentions",
            {
                "fields": (
                    "username",
                    "password",
                )
            },
        ),
        (
            "Personal Infos",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "birthdate",
                    "bio",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_superuser",
                    "is_active",
                    "is_staff",
                    "is_critic",
                )
            },
        ),
        (
            "Importants Dates",
            {
                "fields": (
                    "date_joined",
                    "last_login",
                    "updated_at",
                )
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)
