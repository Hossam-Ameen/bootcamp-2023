from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    class Meta:
        ordering = ['id', 'age']


class AvailableBookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(available=True)


class Book(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    published_year = models.IntegerField()
    published = models.DateField(null=True)
    available = models.BooleanField(default=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    objects = models.Manager()
    avalabile_objects = AvailableBookManager()




class BookDetail(models.Model):
    language = models.CharField(max_length=100)
    page_count = models.IntegerField()
    book = models.OneToOneField(Book, on_delete=models.CASCADE)





class Reader(models.Model):
    name = models.CharField(max_length=100)
    borrowed_books = models.ManyToManyField(Book)
