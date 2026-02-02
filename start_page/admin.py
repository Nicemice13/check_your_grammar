from django.contrib import admin
from .models import Content

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('user', 'language', 'created_at', 'text_preview')
    list_filter = ('language', 'created_at')
    search_fields = ('user__username', 'corrected_text')
    
    def text_preview(self, obj):
        return obj.corrected_text[:50] + '...' if len(obj.corrected_text) > 50 else obj.corrected_text
    text_preview.short_description = 'Превью текста'
