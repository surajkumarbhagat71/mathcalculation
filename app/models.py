from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField()
    phone = models.IntegerField()
    password  = models.CharField(max_length=200)



