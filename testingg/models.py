from django.db import models

# Create your models here.

class Person(models.Model):
    name            = models.CharField(max_length=30)
    brand           = models.CharField(max_length=30)
    description     = models.TextField(max_length=500, blank=True)
    category        = models.TextField(max_length=500, blank=True)
    image           = models.ImageField(upload_to='photos/persons', blank=True)
    stock           = models.CharField(max_length=140, default='SOME STRING')
    code            = models.CharField(max_length=140, default='SOME STRING')
    barcode         = models.CharField(max_length=140, default='SOME STRING')
    price           = models.CharField(max_length=140, default='SOME STRING')
