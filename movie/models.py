from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    category=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category)

        super().save(*args, **kwargs)


    def __str__(self):
        return self.category


class Movie(models.Model):
    movie=models.CharField(max_length=100)
    trailer_link=models.URLField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    release_date=models.DateField()
    poster=models.ImageField(upload_to="poster/")
    description=models.TextField()
    rating=models.DecimalField(max_digits=3,decimal_places=1)
    
    
    actors = models.ManyToManyField(
        'actors.Actors',
        through='MovieCast',
        related_name='movies',
        blank=True
    )

    def __str__(self):
        return self.movie
    
    
class MovieCast(models.Model):

    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE
    )

    actor = models.ForeignKey(
        'actors.Actors',
        on_delete=models.CASCADE
    )

    character_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.actor.name} - {self.character_name}"