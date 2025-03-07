from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Role, Team

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'team', 'role', 'first_name', 'last_name', 'email')
    search_fields = ('username', 'email')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Team and Role', {'fields': ('team', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Team and Role', {'fields': ('team', 'role')}),
    )

# Registering the models
admin.site.register(CustomUser, CustomUserAdmin)  # Use CustomUserAdmin here
admin.site.register(Role)
admin.site.register(Team)