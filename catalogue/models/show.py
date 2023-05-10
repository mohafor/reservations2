from django.db import models
from .location import *
from .artisttype import ArtistType

# Create your models here.
class Show(models.Model):
    slug = models.CharField(max_length=60, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, null=True)
    poster_url = models.CharField(max_length=255, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='shows')
    bookable = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    artist_types = models.ManyToManyField(ArtistType, through='ArtistTypeShow')

    class Meta:
        db_table = "shows"

def __str__(self):
        return f"{self.title} ({self.location})"
