from django.db import models

# Create your models here.

class Book(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    image = models.CharField(max_length=500, default="https://scholastic.asia/sites/all/themes/scholastic_asia/images/default-book.png")
    rating = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    cat = models.CharField(max_length=200)
