from django.urls import path
from . import views

urlpatterns = [
    # Вернули стандартный путь без лишнего префикса href/
    path('book_list/', views.book_list_view, name='book_list'),
    path('about_me/', views.about_me_view, name='about_me'),
    path('contacts/', views.contacts_view, name='contacts'),
]