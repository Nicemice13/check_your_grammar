from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import UserInfo

class UserInfoInline(admin.StackedInline):
    model = UserInfo
    can_delete = False
    readonly_fields = ('photo_preview',)

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="max-height: 200px;"/>', obj.photo.url)
        return "-"
    photo_preview.short_description = 'Превью фото'

admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    inlines = (UserInfoInline,)