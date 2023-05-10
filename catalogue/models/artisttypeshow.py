from django.db import models
from .artisttype import ArtistType
from .show import Show

class ArtistTypeShow(models.Model):
    artist_type = models.ForeignKey(ArtistType, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)

   

    class Meta:
        db_table = 'artist_type_show'