from django.contrib import admin
from django.utils.html import mark_safe
from .models import Asset

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    # Какие поля показывать в таблице (колонки)
    list_display = ('title', 'image_preview', 'created_at', 'id')
    
    # Поля в форме редактирования
    fields = ('title', 'file', 'image', 'image_preview', 'created_at')
    
    # Превью картинки только для чтения
    readonly_fields = ('image_preview',)
    
    # Добавляем строку поиска (поиск по названию)
    search_fields = ('title',) 
    
    # Добавляем фильтр справа (по дате)
    list_filter = ('created_at',)
    
    # Поля, на которые можно кликнуть для входа в редактирование
    list_display_links = ('title',)
    
    def image_preview(self, obj):
        """Показывает миниатюру превью в админке"""
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="70" style="border-radius: 5px;" />')
        return "Нет превью"
    image_preview.short_description = "Превью"
