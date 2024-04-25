from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('full_name', 'preferred_name', 'birthdate', 'picture')}),
        ('Work info', {'fields': ('role', 'boss', 'unit')}),
        ('Contact info', {'fields': ('email', 'phone', 'linkedin', 'github')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('admission_date', 'resignation_date')}),
    )

    list_display = ('username', 'full_name', 'preferred_name', 'email', 'is_active')

    actions = ['alter_active_status']

    def alter_active_status(self, request, queryset):
        for user in queryset:
            user.is_active = not user.is_active
            user.save()

    alter_active_status.short_description = 'Alterar status de atividade'