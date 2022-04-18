from django.db import models
from datetime import datetime


class Book(models.Model):
    title = models.CharField(max_length=200)
    num_pages = models.IntegerField(default=0)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
    price = models.FloatField(default=True, blank=True)
    color = models.CharField(max_length=32, default=True, blank=True)
    isbn13 = models.CharField(max_length=13, blank=True, null=True)

    def __str__(self):
        return self.title
