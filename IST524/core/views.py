from django.http import HttpResponse
from django.shortcuts import render
from . import models


def book_list_view(request):
    # Получаем все книги из базы данных независимо от метода запроса
    books = models.Book.objects.all()
    
    # Передаем их в шаблон (лучше использовать множественное число 'books')
    return render(request, 'book_list.html', {'books': books})



from django.shortcuts import render

def about_me_view(request):
    """Отображает страницу 'О нас'"""
    return render(request, 'about_me.html')



def contacts_view(request):
    return render(request, 'contacts.html')