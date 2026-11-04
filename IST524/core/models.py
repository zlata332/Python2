from django.db import models


class Book(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()
  image = models.ImageField(upload_to="book/")
  author = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.title} - {self.created_at}"

  class Meta:
    verbose_name = "книга"
    verbose_name_plural = "книги" 

    
