from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=10)

    def __str__(self) :
        return self.title
    

class Document(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to="document")
    created_at = models.DateTimeField(auto_now_add=True)
