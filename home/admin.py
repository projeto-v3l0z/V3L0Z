from django.contrib import admin
from .models import Setting, Project, Unit


admin.site.site_header = 'Administração da V3L0Z'
admin.site.site_title = 'V3L0Z'
admin.site.index_title = 'Administração'


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