from django.db import models

# Create your models here.
class Address(models.Model):
    name = models.CharField(max_length=250)
    division = models.CharField(max_length=250)
    population = models.IntegerField()
    area = models.IntegerField()

    def __str__(self):
        return self.name