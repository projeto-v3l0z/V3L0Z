from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('full_name', 'preferred_name', 'birthdate', 'picture')}),
        ('Contact info', {'fields': ('email', 'phone', 'linkedin', 'github')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined', 'admission_date', 'resignation_date')}),
    )

    list_display = ('username', 'full_name', 'preferred_name', 'email', 'is_staff')