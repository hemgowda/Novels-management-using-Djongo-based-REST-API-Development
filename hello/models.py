from unicodedata import name
from django.db import models

# Create your models here.
from django.db import models
class novel(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    cost=models.IntegerField()
    no_of_pages=models.IntegerField()
    author = models.CharField(max_length=200,blank=False, default='')
    publisher = models.CharField(max_length=70, blank=False, default='')
    published = models.BooleanField(default=False)
    edition = models.IntegerField()