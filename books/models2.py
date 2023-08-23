from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    published_year = models.IntegerField()
    available = models.BooleanField(default=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class BookDetail(models.Model):
    language = models.CharField(max_length=50)
    page_count = models.IntegerField()
    book = models.OneToOneField(Book, on_delete=models.CASCADE)


class Reader(models.Model):
    name = models.CharField(max_length=100)
    borrowed_books = models.ManyToManyField(Book)






class AvailableBookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(available=True)



available_objects = AvailableBookManager()