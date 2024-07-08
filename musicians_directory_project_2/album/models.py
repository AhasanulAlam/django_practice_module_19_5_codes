from django.db import models
from musician.models import Musician
from django.utils import timezone


# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=100)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateField(default=timezone.now)
    RATINGS = [
        ('1', 'One'),
        ('2', 'Two'),
        ('3', 'Three'),
        ('4', 'Four'),
        ('5', 'Five'),
    ]
    rating = models.CharField(max_length=1, choices=RATINGS)

    def __str__(self):
        return self.album_name