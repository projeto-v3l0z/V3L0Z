from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Setting, Project, Unit, User


admin.site.site_header = 'Administração da V3L0Z'
admin.site.site_title = 'V3L0Z'
admin.site.index_title = 'Administração'


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['username', 'full_name', 'email', 'is_staff']
    search_fields = ['username', 'full_name', 'email']
    list_filter = ['is_staff']

@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ['about_us_text', 'projects_text', 'how_works_text']
    search_fields = ['about_us_text', 'projects_text', 'how_works_text']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'link']
    search_fields = ['name', 'description']
    list_filter = ['name']



@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['name', 'local', 'description', 'link']
    search_fields = ['name', 'local', 'description']
    list_filter = ['name', 'local']