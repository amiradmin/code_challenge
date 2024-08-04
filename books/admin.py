from django.contrib import admin
from .models import Book,Category

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'isbn', 'user','created_at')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('published_date',)

admin.site.register(Book, BookAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)