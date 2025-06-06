from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'subtitle',
        'author',
    ]


admin.site.register(Book, BookAdmin)