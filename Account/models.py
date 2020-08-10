from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to="Profile", blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)

    def __dir__(self):
        return self.user.username
