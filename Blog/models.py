from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class blog(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    date = models.DateField()
    author = models.CharField(max_length=100, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='Blog')

    def __str__(self):
        return self.title
