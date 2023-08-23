from django.contrib import admin
from django.db.models import QuerySet

from readers.models import Reader


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'is_active']
    list_editable = ['first_name', 'last_name']
    list_filter = ('is_active',)
    actions = ['reverse_status', 'delete_all_books']

    @admin.action(description='Выбрать другую сторону Силы')
    def reverse_status(self, request, status: QuerySet):
        for each_status in status:
            if each_status.is_active:
                status.update(is_active=False)
            else:
                status.update(is_active=True)

    @admin.action(description='Какие книги? Не, не брал')
    def delete_all_books(self, request, reader_books: QuerySet):
        for rb in reader_books:
            rb.books.objects.filter(reader=rb).delete()
