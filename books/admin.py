from django.contrib import admin
from django.db.models import QuerySet
from django.urls import reverse
from django.utils.html import format_html

from books.models import Author, Book

# admin.site.register(Book)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'books_number', 'author_link']
    list_editable = ['title', 'description']
    actions = ['drop_to_zero']

    @admin.action(description='Помножить на ноль')
    def drop_to_zero(self, request, books: QuerySet):
        for book in books:
            book.clear()
            book.save()

    def author_link(self, obj) -> str:
        return format_html(
            "<a href='{url}'>{user_name}</a>",
            url=reverse('admin:books_author_change', kwargs={'object_id': obj.author.id}),
            user_name=f'{obj.author.first_name} {obj.author.last_name}'
        )
    author_link.short_description = 'Автор'

    # def get_related_object(self, obj):
    #     return f'{obj.author.first_name} {obj.author.last_name}'
