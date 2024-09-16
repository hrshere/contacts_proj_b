from django.contrib import admin
from django.utils.html import format_html
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at', 'display_image')
    search_fields = ('name', 'email', 'phone')
    readonly_fields = ('created_at',)

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;"/>', obj.image.url)
        else:
            return '(No image)'

    display_image.short_description = 'Image'
