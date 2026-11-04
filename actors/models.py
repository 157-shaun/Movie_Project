from django.db import models

# Create your models here.
class Actors(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField()
    description=models.TextField()
    place=models.CharField(max_length=100)
    picture=models.ImageField(upload_to="actors/")

    def __str__(self):
        return self.name