from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, default='Горный')

    def __str__(self):
        return self.name


class Tour(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tours'
    )
    leader = models.CharField(
        max_length=100,
        default='Иванов Иван'
    )
    register_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.register_date}'


class Person(models.Model):
    choice_tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE,
        related_name='participants'
    )
    person = models.CharField(
        max_length=100,
        default='Иван Иванов'
    )
    ticket_number = models.CharField(
    max_length=50,
    unique=True,
    null=True,
    blank=True
    )
    created_add = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.person


class Comment(models.Model):
    choice_tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    comment = models.TextField(default='Good tour')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.choice_tour} - {self.created_at}'