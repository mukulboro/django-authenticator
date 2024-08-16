from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ExtendedUser

class ExtendedUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('has_2fa',)}),  # Add your new field here
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('has_2fa',)}),  # Add your new field here
    )

admin.site.register(ExtendedUser, ExtendedUserAdmin)
