from django.db import models

class Product(models.Model):
  tittle = models.CharField(max_length=200)
  image = models.CharField(max_length=200)
  likes = models.PositiveIntegerField(default=0)
  objects = models.Manager()

class User(models.Model):
  objects = models.Manager()
  pass