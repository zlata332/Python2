
from django.shortcuts import render, get_object_or_404
from django.db.models import F
from . import models


def book_list_view(request):
    books = models.Book.objects.all()

    return render(request, 'book_list.html', {
        'books': books
    })


def book_detail_view(request, pk):
    book = get_object_or_404(models.Book, pk=pk)

    # Проверяем, является ли пользователь администратором
    if not request.user.is_staff:

        # Создаём уникальный ключ для каждой книги
        session_key = f'viewed_book_{book.pk}'

        # Проверяем, смотрел ли пользователь эту книгу
        if not request.session.get(session_key):

            # Увеличиваем просмотры
            models.Book.objects.filter(pk=pk).update(
                views=F('views') + 1
            )

            # Запоминаем просмотр в сессии
            request.session[session_key] = True

            book.refresh_from_db()

    return render(request, 'book_detail.html', {
        'book': book
    })


def about_me_view(request):
    return render(request, 'about_me.html')


def contacts_view(request):
    return render(request, 'contacts.html')
