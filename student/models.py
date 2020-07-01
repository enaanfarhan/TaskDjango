from django.db import models


class StudentDetail(models.Model):
    name = models.CharField(max_length=250)
    roll = models.IntegerField()
    gender = models.CharField(max_length=10)
    department = models.CharField(max_length=10)

    def __str__(self):
        return self.name