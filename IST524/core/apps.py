from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'

class BookConfig(AppConfig):
    name = 'book'
    verbose_name = 'книги'