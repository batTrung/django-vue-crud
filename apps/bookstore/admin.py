from django.contrib import admin
from django.utils.html import format_html

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    def photo_display(self, obj):
        return format_html(f'<img src="{obj.photo}" style="width: 50px; height:50px;" />')

    list_display = ('name', 'description', 'author', 'views', 'photo_display',)
    search_fields = ('name', 'description',)
