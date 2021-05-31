from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.TextField()
    email=models.TextField()
    message=models.TextField()
    date=models.DateField()
    def __str__(self):
            return self.name