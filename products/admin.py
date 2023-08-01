from django.contrib import admin
from django.utils.html import format_html  
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image_preview', 'external_link']

    def image_preview(self, obj):
        return format_html('<img src="{}" style="height: 50px; width: auto;" />', obj.image.url)

    image_preview.short_description = 'Image Preview'
fieldsets = (
        ('Product Information', {
            'fields': ('name', 'description', 'image', 'external_link')
        }),
    )

admin.site.register(Product, ProductAdmin)
