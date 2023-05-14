from django.db import models
from .artist import Artist
from .type import Type
from .show import *



class ArtistType(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    

    class Meta:
        db_table = "artist_type"
