from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.category

class product(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField()
    description = models.CharField(max_length=500)
    image = models.ImageField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name