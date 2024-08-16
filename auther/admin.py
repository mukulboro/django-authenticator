from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ExtendedUser

class ExtendedUserAdmin(UserAdmin):
    # Since we overrode the default User model, including new model in admin panel
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('has_2fa',)}), 
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('has_2fa',)}), 
    )

admin.site.register(ExtendedUser, ExtendedUserAdmin)
