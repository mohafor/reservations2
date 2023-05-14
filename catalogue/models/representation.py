from django.db import models
from .location import *
from .show import *


# Create your models here.
class Representation(models.Model):
    show = models.ForeignKey(Show, on_delete=models.SET_NULL, null=True, related_name='representations')
    schedule = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='representations')

    class Meta:
        db_table = "representations"