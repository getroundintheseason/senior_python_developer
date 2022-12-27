from django.db import models

# Create your models here.
class Coffee(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    bean_from = models.CharField(max_length=200, null=True, blank=True)
    price = models.IntegerField()



