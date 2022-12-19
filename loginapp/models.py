from django.db import models

# Create your models here.
class Adv(models.Model):
    name = models.CharField(max_length=50)
    des = models.TextField()
