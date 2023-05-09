from django.db import models
from .artist import *

# Create your models here.
class Type(models.Model):
	type = models.CharField(max_length=60)
	artists = models.ManyToManyField('catalogue.Artist', through='ArtistType')

	def __str__(self):
		return f"{self.type}"
	
	class Meta:
		db_table = "types"
