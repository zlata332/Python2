
from django.db import models

class Finance(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Какие траты у вас сегодня?'
    )

    description = models.TextField(
        verbose_name='Опишите их:',
        blank=True
    )

    CHEKING = (
        ('Расход', 'Расход'),
        ('Доход', 'Доход'),
        ('Не выбрано', 'Не выбрано'),
    )

    cheking = models.CharField(
        max_length=100,
        default='Не выбрано',
        choices=CHEKING,
        verbose_name='Выберите вариант'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
