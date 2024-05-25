# book_orders/admin.py

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import BookOrder, Book, Class

class BookOrderResource(resources.ModelResource):
    class Meta:
        model = BookOrder
        fields = ('id', 'name', 'phone', 'selected_class__name', 'total_amount', 'books')
        export_order = ('id', 'name', 'phone', 'selected_class__name', 'total_amount', 'books')

    def dehydrate_books(self, book_order):
        return ", ".join([book.name for book in book_order.books.all()])

@admin.register(BookOrder)
class BookOrderAdmin(ImportExportModelAdmin):
    resource_class = BookOrderResource
    list_display = ('name', 'phone', 'selected_class', 'total_amount')
    search_fields = ('name', 'phone')
    filter_horizontal = ('books',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('available_classes',)
    search_fields = ('name',)
    filter_horizontal = ('available_classes',)

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
