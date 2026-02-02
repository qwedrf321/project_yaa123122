from django.contrib import admin
from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'folder', 'is_public', 'created_at', 'updated_at')
    list_filter = ('is_public', 'created_at', 'folder', 'owner')
    search_fields = ('title', 'content')
    readonly_fields = ('created_at', 'updated_at')
    raw_id_fields = ('owner', 'folder')

    fieldsets = (
        ('Основна інформація', {
            'fields': ('title', 'owner', 'folder')
        }),
        ('Контент', {
            'fields': ('content',),
            'classes': ('wide',)
        }),
        ('Налаштування', {
            'fields': ('is_public',)
        }),
        ('Мітки часу', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


admin.site.register(Note, NoteAdmin)
