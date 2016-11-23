from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=31)
    slug = models.SlugField()

class Startup(models.Model):
    name = models.CharField(max_length=31)
    slug = models.SlugField()
    descrription = models.TextField()
    founded_date = models.DateField()
    contact = models.EmailField()
    website = models.URLField()

class NewsLink(models.Model):
    pass
